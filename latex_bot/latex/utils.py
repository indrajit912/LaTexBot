# Some utility funtions for Latex
# Author: Indrajit Ghosh
# Date: Jul 20, 2023
#

import tempfile, shutil, platform, subprocess, os
from pathlib import Path

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


def main():
    _clear_tex_output_files(tex_dir=Path.cwd())


if __name__ == '__main__':
    main()
    