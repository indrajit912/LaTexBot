# A script to create a blank thesis
#
# Author: Indrajit Ghosh
#
# Date: December 17, 2021
#
# Status: Ongoing...
#

from pathlib import Path
import shutil, subprocess, os

from templates.main_tex import MAIN
from templates.bibliography_bib_tex import REFERENCES
from templates.style_ist_tex import STYLE

from templates.thesis_structure_tex import THESIS_STRUCTURE
from templates.math_constants_tex import MATH_CONSTANTS

from templates.chapters_tex import *


HOME = Path.home()
CWD = Path.cwd()

COMPILE_TEX_LIVES_HERE = HOME / "Documents/latex_files/scripts_for_tex/latex_bot/compile_tex.py"

def setup_output_directory():

    output_directory = CWD / "new_thesis"
    Path.mkdir(output_directory)
    
    imgs = output_directory / "Images"
    Path.mkdir(imgs)

    chapters = output_directory / "Chapters"
    Path.mkdir(chapters)

    img_file = HOME / "Documents/latex_files/scripts_for_tex/thesis_bot/templates/latex.jpeg"
    shutil.copy(img_file, imgs)


    bib_filename = output_directory / "bibliography.bib"
    with open(bib_filename, "w") as f:
        f.write(REFERENCES)

    style_ist = output_directory / "style.ist"
    with open(style_ist, "w") as f:
        f.write(STYLE)

    return output_directory


def create_math_constants_tex(output_dir):
    print(MATH_CONSTANTS)

    filename = output_dir / "math_constants.tex"
    with open(filename, "w") as f:
        f.write(MATH_CONSTANTS)


def create_thesis_structure_tex(output_dir):

    with open(output_dir / "thesis_structure.tex", "w") as f:
        f.write(THESIS_STRUCTURE)

    print(THESIS_STRUCTURE)


def write_chapters(output_dir):

    chapters_dir = output_dir / "Chapters"

    titlepage = chapters_dir / "titlepage.tex"
    with open(titlepage, "w") as f:
        f.write(TITLEPAGE)

    abstract = chapters_dir / "abstract.tex"
    with open(abstract, "w") as f:
        f.write(ABSTRACT)

    dedication = chapters_dir / "dedication.tex"
    with open(dedication, "w") as f:
        f.write(DEDICATION)

    declaration = chapters_dir / "declaration.tex"
    with open(declaration, "w") as f:
        f.write(DECLARATION)

    acknowledgements = chapters_dir / "acknowledgements.tex"
    with open(acknowledgements, "w") as f:
        f.write(ACKNOWLEDGEMENTS)

    introduction = chapters_dir / "introduction.tex"
    with open(introduction, "w") as f:
        f.write(INTRODUCTION)

    chap_1 = chapters_dir / "chapter01.tex"
    with open(chap_1, "w") as f:
        f.write(CHAPTER_1)

    chap_2 = chapters_dir / "chapter02.tex"
    with open(chap_2, "w") as f:
        f.write(CHAPTER_2)

    chap_3 = chapters_dir / "chapter03.tex"
    with open(chap_3, "w") as f:
        f.write(CHAPTER_3)

    conclusion = chapters_dir / "conclusion.tex"
    with open(conclusion, "w") as f:
        f.write(CONCLUSION)

    appendix = chapters_dir / "appendix.tex"
    with open(appendix, "w") as f:
        f.write(APPENDIX)



def create_main_tex(output_dir):

    with open(output_dir / "main.tex", "w") as f:
        f.write(MAIN)

    print(MAIN)
    
    
def main():

    output_directory_path = setup_output_directory()

    create_math_constants_tex(output_directory_path)
    create_thesis_structure_tex(output_directory_path)

    # Chapters
    write_chapters(output_directory_path)

    # Main.tex
    create_main_tex(output_directory_path)

    os.chdir(output_directory_path)
    subprocess.run(["python3", str(COMPILE_TEX_LIVES_HERE)])

    os.system('clear')

    print(f"\n\n\t\t::: YOUR TeX WORKING DIRECTORY :::\n\n   {output_directory_path}\n\n")


if __name__ == "__main__":

    main()
