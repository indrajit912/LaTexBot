# Some utility funtions for Latex
# Author: Indrajit Ghosh
# Date: Jul 20, 2023
#

import tempfile, shutil, platform, subprocess, os
from pathlib import Path
import fnmatch, sys

TEX_ERROR_FOUND = (
    "\n"
    + '\x1b[38;2;255;0;0m' # red
    + '\033[5m' # blink
    + '\033[1m' # bold
    + "\t\t -- LaTeX ERROR -- " 
    + '\033[0m'
    + "\n"
)

PATTERNS_TO_DELETE = [
    '*.aux', '*.bbl', '*.blg', '*.out', '*.toc',
    '*.synctex.gz', '*.gz', '*.log', "*-blx.bib",
    "*.run.xml", "*.bcf", "*.snm", "*.nav",
    "*.fdb_latexmk", "*.fls", "*.acr", "*.idx",
    "*.ilg", "*.ind", "*.vrb"
]

def make_temp_dir():
    """
    Create a temporary directory if it doesn't exist.

    Returns
    -------
    str
        The absolute filepath to the created temporary directory.

    Examples
    --------
    >>> make_temp_dir()
    """

    global _tmp_path
    if not _tmp_path:
        _tmp_path = tempfile.mkdtemp(prefix="latexbot-tmp.")
    return _tmp_path


def rm_temp_dir():
    """Remove the temporary directory specified in ``_tmp_path``."""

    global _tmp_path
    if _tmp_path:
        shutil.rmtree(_tmp_path)
        _tmp_path = None


def open_file(file_path, in_browser=False):
    current_os = platform.system()
    if current_os == "Windows":
        os.startfile(file_path if not in_browser else file_path.parent)
    else:
        if current_os == "Linux":
            commands = ["xdg-open"]
            file_path = file_path if not in_browser else file_path.parent
        elif current_os.startswith("CYGWIN"):
            commands = ["cygstart"]
            file_path = file_path if not in_browser else file_path.parent
        elif current_os == "Darwin":
            
                commands = ["open"] if not in_browser else ["open", "-R"]
        else:
            raise OSError("Unable to identify your operating system...")
        commands.append(file_path)
        subprocess.Popen(commands)


def filename_matches_patterns(filename, patterns):
    """
    Checks if the given filename matches one of the patterns in the patterns list.
    
    Parameters:
        filename (str): The filename to check.
        patterns (list): List of patterns to match against the filename.
                        e.g - ["*.txt", "data_*.csv", "*.png"]
        
    Returns:
        bool: True if the filename matches one of the patterns, False otherwise.
    """
    return any(fnmatch.fnmatch(filename, pattern) for pattern in patterns)


def _clear_tex_output_files(tex_dir: Path):
    """
    This function deletes all output files such as `.aux`, `.bbl`, etc., from the given directory.
    """
    tex_dir = Path(tex_dir)

    if not tex_dir.exists():
        raise FileNotFoundError(f"No such directory found with location: {tex_dir}")

    for f in tex_dir.glob('*'):
        if filename_matches_patterns(f.name, PATTERNS_TO_DELETE):
            f.unlink()

    print("\nAll LaTeX output files deleted!\n")


def tex_compilation_commands(tex_compiler:str, tex_file:Path):
    r"""
    Prepares the tex compilation command with all necessary cli flags

    Parameters
    ----------
    tex_compiler
        String containing the compiler to be used, e.g. ``pdflatex`` or ``lualatex``
    output_format
        String containing the output format generated by the compiler, e.g. ``.dvi`` or ``.pdf``
    tex_file
        File name of TeX file to be typeset.
    output_dir
        Path to the directory where compiler output will be stored.

    Returns
    -------
    :class:`list`
        Compilation commands according to given parameters this list can be used
        to pass into `subprocess.run()`
    """

    if tex_compiler in {"latex", "pdflatex", "luatex", "lualatex", "xelatex"}:
        commands = [
            tex_compiler,
            "-interaction=batchmode",
            "-synctex=1",
            "-halt-on-error",
            f'"{tex_file.as_posix()}"'
        ]
    else:
        raise ValueError(f"Tex compiler {tex_compiler} unknown.")
    
    return commands

def compile_tex(
        texfile:Path, 
        tex_compiler:str='pdflatex', 
        output_format:str='.pdf', 
        backend: str = "bibtex"
):
    """
    Compiles a `TeX` file and opens the output
    """
    
    try:
        # Set up TeX file
        texfile = Path(texfile)

        if not texfile.exists():
            raise FileNotFoundError(
                f"No TeX file found: '{texfile}'\n"
            )

        _cmds = tex_compilation_commands(
            tex_compiler=tex_compiler,
            tex_file=texfile
        )

    except FileNotFoundError as e:
        print(f"NO_TEX_FILE_FOUND: {e}")
        sys.exit(1)

    tex_compiler_cwd:Path = texfile.parent.resolve()

    print(f"\n- Compiling using `{tex_compiler}` ...")
    res = subprocess.run(_cmds, stdout=subprocess.DEVNULL, cwd=tex_compiler_cwd)

    if res.returncode != 0:
        log_file = texfile.with_suffix('.log')
        _print_tex_error_from_log(
            log_file=log_file,
            tex_compiler=tex_compiler
        )
        sys.exit(1)
    
    if backend in {"bibtex", "biber"}:
        aux_file = texfile.with_suffix(".aux").name if backend == 'bibtex' else texfile.name.rstrip(".tex")

        # Run the appropriate bibliography backend
        print(f"- Compiling using `{backend}` ...")
        subprocess.run([backend, aux_file], stdout=subprocess.DEVNULL, cwd=tex_compiler_cwd)

        # Recompile for cross-references
        print(f"- Compiling using `{tex_compiler}` ...")
        subprocess.run(_cmds, stdout=subprocess.DEVNULL, cwd=tex_compiler_cwd)
        print(f"- Compiling using `{tex_compiler}` ...")
        subprocess.run(_cmds, stdout=subprocess.DEVNULL, cwd=tex_compiler_cwd)

    
    output_file = texfile.with_suffix(output_format)
    if output_file.exists():
        open_file(output_file)


def _print_tex_error_from_log(log_file:Path, tex_compiler:str='pdflatex'):
    """
    Prints the TeX errors from the `log_file`
    """
    if not log_file.exists():
        raise RuntimeError(
            f"`{tex_compiler}` failed but did not produce a log file. "
            "Check your LaTeX installation.",
        )
    
    with log_file.open(encoding="utf-8") as f:
        tex_log = f.readlines()
    
    err_index = None
    for index, line in enumerate(tex_log):
        if line.startswith("!"):
            err_index = index
            break

    err_msg = (
        TEX_ERROR_FOUND
        + "".join(tex_log[err_index:])
    )
    
    print(err_msg)


def is_latex_installed():
    """
    This function checks whether a LaTeX distribution is installed on the system.
    """
    try:
        # Attempt to execute pdflatex command
        subprocess.run(['pdflatex', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except FileNotFoundError:
        # pdflatex command not found, hence LaTeX distribution is not installed
        return False
    except subprocess.CalledProcessError:
        # pdflatex command returned an error, but it means LaTeX is installed
        # We assume that the command is installed but there might be some error in the execution.
        return True


def main():
    _clear_tex_output_files(tex_dir=Path.cwd())


if __name__ == '__main__':
    main()
    