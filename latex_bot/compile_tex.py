# A script to compile a tex file
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
#

from pathlib import Path
import subprocess, sys, os


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


def get_tex_compilation_command(
    tex_compiler: str,
    output_format: str,
    tex_file:Path,
    tex_dir:Path
):
    """
    Returns the command to compile a TeX file

    Parameters:
    -----------
        `tex_compiler`: `str`, e.g- 'latex', 'pdflatex', 'xelatex' etc
        `output_format: `str`, e.g.- '.pdf', '.dvi' etc
        `tex_file`: `Path`, path of the TeX file to compile
        `tex_dir`: `Path`, path of the directory where to compile. Ffiles created
                        during the compilation will be stored in this directory.

    Returns:
    --------
        `str`
    """
    if tex_compiler in {"latex", "pdflatex", "luatex", "lualatex"}:

        cli_flags = [
            tex_compiler,
            "-interaction=batchmode",
            f'-output-format="{output_format[1:]}"',
            "-halt-on-error",
            f'-output-directory="{tex_dir.as_posix()}"',
            f'"{tex_file.as_posix()}"',
            ">",
            os.devnull,
        ]

    elif tex_compiler == 'xelatex':
        if output_format == ".xdv":
            outputflag = "-no-pdf"
        elif output_format == ".pdf":
            outputflag = ""
        else:
            raise ValueError("xelatex output is either pdf or xdv")

        cli_flags = [
            "xelatex",
            outputflag,
            "-interaction=batchmode",
            "-halt-on-error",
            f'-output-directory="{tex_dir.as_posix()}"',
            f'"{tex_file.as_posix()}"',
            ">",
            os.devnull,
        ]

    else:
        raise ValueError(f"TeX compiler `{tex_compiler}` is unknown.")

    return " ".join(cli_flags)


def compile_tex(tex_file:Path, tex_compiler:str, output_format:str, tex_dir:Path=None):
    """
    Compiles a TeX file into `.pdf` or `.dvi` and returns the path of that `.pdf` (or `dvi)

    Parameters:
    -----------
        `tex_file`: Path; path of the TeX file to compile
        `tex_compiler`: `str`, e.g- 'latex', 'pdflatex', 'xelatex' etc
        `output_format: `str`, e.g.- '.pdf', '.dvi' etc
        `tex_dir`: `Path`; this is the path to the dir where the compiled files will be stored
                    by default it is the parent dir of `tex_file`

    Returns:
    --------
        `Path`: path to the generated `.pdf` file
    """
    generated_file = tex_file.with_suffix(output_format)
    tex_dir = tex_file.parent if tex_dir is None else tex_dir

    command = get_tex_compilation_command(
        tex_compiler=tex_compiler,
        output_format=output_format,
        tex_file=tex_file,
        tex_dir=tex_dir
    )

    exit_code = os.system(command)
    if exit_code != 0:
        log_file = tex_file.with_suffix(".log")
        print(f"ERROR: some unexpected thing occured, check the `.log` file: {log_file}")

    return generated_file


def compile_texfile_to_pdf(texfile:Path):
    """
    Use `compile_tex()` to compiles the given `texfile` and opens the generated pdf 
    """
    texfile = Path(texfile)
    aux_file = texfile.with_suffix(".aux")
    pdf = texfile.with_suffix(".pdf")

    with open(texfile, 'r') as f:
        if "metropolis" in f.read():
            commented_metropolis = r"""%\usetheme{metropolis}""" in f.read()
            tex_compiler = 'pdflatex' if commented_metropolis else 'xelatex'
        else:
            tex_compiler = 'pdflatex'

    print(f" - Compiling using {tex_compiler}")
    compile_tex(tex_file=texfile, tex_compiler=tex_compiler, output_format='.pdf')

    print(f" - Compiling using bibtex")
    os.system(f"bibtex {aux_file} > {os.devnull}") # compiling `.aux` file

    print(f" - Compiling using {tex_compiler}")
    compile_tex(tex_file=texfile, tex_compiler=tex_compiler, output_format='.pdf')
    print(f" - Compiling using {tex_compiler}")
    compile_tex(tex_file=texfile, tex_compiler=tex_compiler, output_format='.pdf')

    print("\n\n:::NOTE::: Successfully complied!\n\n")

    os.system(f"xdg-open {pdf}")



# def compile_tex(texfilepath:Path):
#     """
#     This function takes a texfile's absolute Path and compiles
#     it in the following manner:

#         pdflatex <main.tex>
#         bibtex <main.aux>
#         pdflatex <main.tex>
#         pdflatex <main.tex>
    
#     """

#     texcompilers ={
#         "pdf" : "pdflatex",
#         "xe" : "xelatex",
#         "lua" : "lualatex"
#     }

#     texfilepath = Path(texfilepath)

#     parent_dir = texfilepath.parent
#     texfilename = texfilepath.name

#     with open(texfilename, 'r') as f:
#         if "metropolis" in f.read():
#             commented_metropolis = r"""%\usetheme{metropolis}""" in f.read()

#             if commented_metropolis:
#                 compiler = texcompilers['pdf']
#             else:
#                 compiler = texcompilers['xe']
#         else:
#             compiler = texcompilers['pdf']

#     subprocess.run([compiler, texfilename]) # compiling `main.tex`

#     auxfilename = texfilename[:-4] + ".aux"

#     subprocess.run(["bibtex", auxfilename]) # compiling `main.aux`

#     subprocess.run([compiler, texfilename]) # compiling `main.tex`
#     subprocess.run([compiler, texfilename]) # compiling `main.tex`

#     print("\n\n:::NOTE::: Successfully complied!\n\n")


#     pdfname = texfilename[:-4] + ".pdf"
#     subprocess.run(['xdg-open', pdfname]) # opening `main.pdf`


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