# A script to compile a tex file
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
# Modified on: Dec 11, 2022
#

from pathlib import Path
import sys, os, platform
import subprocess


HOME = Path.home()
CWD = Path.cwd()

from latex import open_file, compile_tex


def _open_file(filepath:Path):
    """
    This function can open file at `filepath` using the platform's 
    default application.
    """
    filepath = Path(filepath)
    
    if platform.system() == "Darwin":
        subprocess.call(('open', filepath)) # MacOS

    elif platform.system() == "Windows":
        os.startfile(filepath)  # Windows

    else:
        subprocess.call(('xdg-open', filepath)) # Linux


def list_files(path):
    """
    Returns the lists containg AbsolutePaths of files
    at the given path
    """
    given_path = Path.absolute(path)
    files = []

    for file_or_dir in given_path.glob('*'):
        if file_or_dir.is_file():
            files.append(file_or_dir)

    # p = Path.absolute(files[0]) # Getting the absolute path

    return files


def compile_texfile_to_pdf(texfile:Path):
    """
    Use `compile_tex()` to compiles the given `texfile` and opens the generated pdf 
    """
    texfile = Path(texfile)

    with open(texfile, 'r') as f:
        if "metropolis" in f.read():
            commented_metropolis = r"""%\usetheme{metropolis}""" in f.read()
            _tex_compiler = 'pdflatex' if commented_metropolis else 'xelatex'
        else:
            _tex_compiler = 'pdflatex'

    _bib_files = []
    for f in texfile.parent.glob('*.bib'):
        _bib_files.append(f)
    
    _use_bibtex = (
        True
        if _bib_files
        else False
    )
    
    compile_tex(
        main_tex=texfile,
        tex_dir=texfile.parent,
        tex_compiler=_tex_compiler,
        bibtex=_use_bibtex
    )



def main():

    if len(sys.argv) < 2:

        main_tex_file = CWD / "main.tex"

        if main_tex_file.exists():
            compile_texfile_to_pdf(main_tex_file)

        else:
            # Usages
            print(
                """
                USAGES: compile_tex.py

                    compiletex <main.tex>

                """
            )
            sys.exit()

    else:
        texfile = CWD / sys.argv[1]

        compile_texfile_to_pdf(texfile)


if __name__ == '__main__':
    main()