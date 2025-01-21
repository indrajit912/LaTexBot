# A script to compile a tex file
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
# Modified on: Dec 11, 2022
#

from pathlib import Path
import sys
import re


HOME = Path.home()
CWD = Path.cwd()

from latex import compile_tex


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


def determine_bibliography_backend(texfile: Path) -> str:
    r"""
    Determines whether to use `biber` or `bibtex` based on the presence of `\usepackage{biblatex}`.
    Handles cases where `biblatex` is used with or without options.
    """
    preamble_file = texfile.parent / "preamble.tex"
    use_biblatex = False
    biblatex_pattern = re.compile(r"\\usepackage(\[[^\]]*\])?\{biblatex\}")

    try:
        # Check the main TeX file for biblatex
        with open(texfile, "r") as f:
            if re.search(biblatex_pattern, f.read()):
                use_biblatex = True

        # Check preamble.tex if it exists
        if preamble_file.exists():
            with open(preamble_file, "r") as f:
                if re.search(biblatex_pattern, f.read()):
                    use_biblatex = True
    except Exception as e:
        print(f"Error reading files: {e}")
        sys.exit(1)

    return "biber" if use_biblatex else "bibtex"


def compile_texfile_to_pdf(texfile: Path):
    """
    Compiles the given TeX file to PDF, dynamically selecting the bibliography backend.
    """
    texfile = Path(texfile)
    try:
        # Determine the TeX compiler (check for Metropolis theme)
        with open(texfile, "r") as f:
            tex_content = f.read()
            if "metropolis" in tex_content:
                commented_metropolis = r"""%\usetheme{metropolis}""" in tex_content
                tex_compiler = "pdflatex" if commented_metropolis else "xelatex"
            else:
                tex_compiler = "pdflatex"

        # Determine the bibliography backend
        backend = determine_bibliography_backend(texfile)

        compile_tex(
            texfile=texfile,
            tex_compiler=tex_compiler,
            output_format=".pdf",
            backend=backend
        )

    except FileNotFoundError as e:
        print(f"NO_TEX_FILE_FOUND: {e}")


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