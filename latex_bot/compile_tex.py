# A script to compile a tex file
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
#

from pathlib import Path
import subprocess, sys


HOME = Path.home()
CWD = Path.cwd()

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


def compile_tex(texfilepath:Path):
    """
    This function takes a texfile's absolute Path and compiles
    it in the following manner:

        pdflatex <main.tex>
        bibtex <main.aux>
        pdflatex <main.tex>
        pdflatex <main.tex>
    
    """

    texcompilers ={
        "pdf" : "pdflatex",
        "xe" : "xelatex",
        "lua" : "lualatex"
    }

    texfilepath = Path(texfilepath)

    parent_dir = texfilepath.parent
    texfilename = texfilepath.name

    with open(texfilename, 'r') as f:
        if "metropolis" in f.read():
            commented_metropolis = r"""%\usetheme{metropolis}""" in f.read()

            if commented_metropolis:
                compiler = texcompilers['pdf']
            else:
                compiler = texcompilers['xe']
        else:
            compiler = texcompilers['pdf']

    subprocess.run([compiler, texfilename]) # compiling `main.tex`

    auxfilename = texfilename[:-4] + ".aux"

    subprocess.run(["bibtex", auxfilename]) # compiling `main.aux`

    subprocess.run([compiler, texfilename]) # compiling `main.tex`
    subprocess.run([compiler, texfilename]) # compiling `main.tex`

    print("\n\n:::NOTE::: Successfully complied!\n\n")


    pdfname = texfilename[:-4] + ".pdf"
    subprocess.run(['xdg-open', pdfname]) # opening `main.pdf`


def main():

    if len(sys.argv) < 2:

        main_tex_file = CWD / "main.tex"

        if main_tex_file.exists():
            compile_tex(main_tex_file)

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

        compile_tex(texfile)


if __name__ == '__main__':
    main()