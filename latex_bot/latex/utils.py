# Some utility funtions for Latex
# Author: Indrajit Ghosh
# Date: Jul 20, 2023
#

import tempfile, shutil, platform, subprocess, os
from pathlib import Path

TEX_ERROR_FOUND = (
    "\n"
    + '\x1b[38;2;255;0;0m' # red
    + '\033[5m' # blink
    + '\033[1m' # bold
    + "\t\t -- LaTeX ERROR -- " 
    + '\033[0m'
    + "\n"
)

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


def _clear_tex_output_files(tex_dir:Path):
    """
    This function deletes all output files such as `.aux`, `.bbl` etc 
    from the given dir
    """
    _to_del = [
        '.aux', '.bbl', '.blg', '.out', '.toc',
        '.synctex.gz', '.gz', '.log'
    ]
    tex_dir = Path(tex_dir)

    if not tex_dir.exists():
        raise FileNotFoundError(f"No such dir found with location: {tex_dir}")
    
    
    for f in tex_dir.glob("*"):
        if f.is_file() and f.suffix in _to_del:
            f.unlink()

    print("\nAll LaTeX output files deleted!\n")


def tex_compilation_commands(tex_compiler: str, tex_file: Path):
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
    tex_dir
        Path to the directory where compiler output will be stored.

    Returns
    -------
    :class:`list`
        Compilation commands according to given parameters this list can be used
        to pass into `subprocess.run()`
    """
    if tex_compiler in {"latex", "pdflatex", "luatex", "lualatex"}:
        commands = [
            tex_compiler,
            "-interaction=batchmode",
            "-halt-on-error",
            f'"{tex_file.as_posix()}"'
        ]
    else:
        raise ValueError(f"Tex compiler {tex_compiler} unknown.")
    
    return commands

def compile_tex(main_tex:str, tex_dir:Path, tex_compiler:str='pdflatex', bibtex:bool=True):
    """
    Compiles a `TeX` file and opens the output
    """
    os.chdir(tex_dir)

    main_tex:Path = Path(tex_dir) / main_tex

    main_aux = main_tex.with_suffix('.aux').name
    main_pdf = main_tex.with_suffix('.pdf')

    _cmds = tex_compilation_commands(
        tex_compiler=tex_compiler,
        tex_file=main_tex
    )

    print(f"\n- Compiling using `{tex_compiler}` ...")
    res = subprocess.run(_cmds, stdout=subprocess.PIPE)

    if res.returncode != 0:
        log_file = main_tex.with_suffix(".log")
        raise RuntimeError(f"ERROR: some unexpected thing occured, check the `.log` file: {log_file}")


    if bibtex:
        print(f"- Compiling using `bibtex` ...")
        subprocess.run(['bibtex', main_aux], stdout=subprocess.PIPE)

        print(f"- Compiling using `{tex_compiler}` ...")
        subprocess.run(_cmds, stdout=subprocess.PIPE)

        print(f"- Compiling using `{tex_compiler}` ...\n")
        subprocess.run(_cmds, stdout=subprocess.PIPE)

    
    if main_pdf.exists():
        open_file(main_pdf)


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


def main():
    _clear_tex_output_files(tex_dir=Path.cwd())


if __name__ == '__main__':
    main()
    