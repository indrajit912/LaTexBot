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
    Determines whether to use `biber` or `bibtex` based on the `backend` option in `\usepackage{biblatex}`.
    If no `\usepackage{biblatex}` is found, defaults to `bibtex`.
    """
    preamble_file = texfile.parent / "preamble.tex"
    
    # Regex to match \usepackage{biblatex} with optional arguments (e.g., [backend=biber,style=alphabetic]).  
    biblatex_pattern = re.compile(r"\\usepackage(\[([^\]]*)\])?\{biblatex\}")

    def find_backend_in_file(file_path: Path) -> str:
        """Searches for the backend in the given file."""
        try:
            with open(file_path, "r") as f:
                for line in f:
                    match = re.search(biblatex_pattern, line)
                    if match:
                        options = match.group(2)  # Extract options inside [...]
                        if options:
                            backend_match = re.search(r"backend=(\w+)", options)
                            if backend_match:
                                return backend_match.group(1)  # Return the backend value
                        return "biber"  # Default to biber if backend is not explicitly set
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
        return None

    # Check the main TeX file
    backend = find_backend_in_file(texfile)
    if backend:
        return backend

    # Check the preamble.tex file if it exists
    if preamble_file.exists():
        backend = find_backend_in_file(preamble_file)
        if backend:
            return backend

    # Default to bibtex if no \usepackage{biblatex} is found
    return "bibtex"


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