# A script to create a blank article template
#
# Author: Indrajit Ghosh
#
# Date: November, 2021
#
# Status: Ongoing...
#
#  Commands for genrating pdf
#       1. pdflatex <main.tex>
#       2. bibtex <main.aux>
#       3. pdflatex <main.tex>
#

from pathlib import Path
import subprocess, os

from templates.main_tex import main_tex_constants
from templates.structure_tex import structure_tex_constants
from templates.math_constants_tex import MATH_CONSTANTS
from templates.bibliography_bib import BIBLIOGRAPHY
from templates.sections_tex import SECTIONS

HOME = Path.home()
CWD = Path.cwd()

COMPILE_TEX_LIVES_HERE = HOME / "Documents/latex_files/scripts_for_tex/latex_bot/compile_tex.py"

def setup_output_directory():

    output_directory = CWD / "new_article"
    Path.mkdir(output_directory)

    sections = output_directory / "sections"
    Path.mkdir(sections)

    with open(sections / "section1.tex", "w") as f:
        f.write(SECTIONS['1'])

    with open(sections / "section2.tex", "w") as f:
        f.write(SECTIONS['2'])
    
    imgs = output_directory / "images"
    Path.mkdir(imgs)

    return output_directory


def create_math_constants_tex(output_dir):
    print(MATH_CONSTANTS)

    filename = output_dir / "math_constants.tex"
    with open(filename, "w") as f:
        f.write(MATH_CONSTANTS)


def create_structure_tex(info:dict, output_dir):

    s1, s4 = structure_tex_constants

    bibliography_filename = "bibliography.bib"

    title = info['title']
    author = info['author']

    s2 = "    pdftitle={" + title + "},\n"
    s3 = "    pdfauthor={" + author + "},"
    s5 = "\\addbibresource{" + bibliography_filename + "} % The filename of the bibliography"

    tex_string = s1 + s2 + s3 + s4 + s5

    with open(output_dir / "structure.tex", "w") as f:
        f.write(tex_string)

    with open(output_dir / "bibliography.bib", "w") as b:
        b.write(BIBLIOGRAPHY)

    print(BIBLIOGRAPHY)
    print(tex_string)


def create_main_tex(info:dict, output_dir):

    title = info['title']
    authorname = info['author']
    email = info['email']
    dept = info['dept']
    institute = info['institute']
    country = info['country']

    m1, m4, m6 = main_tex_constants
    m2 = r"""\title{""" + title + "}\n"
    m3 = r"""\author[1]{""" + authorname + r"""\thanks{Email: """ + email + "}}\n"
    m5 = r"""\affil[1]{\small{""" + dept + r""", \textcolor{olive}{""" + institute + r"""}}}"""

    tex_string = m1 + m2 + m3 + m4 + m5 + m6

    with open(output_dir / "main.tex", "w") as f:
        f.write(tex_string)

    print(tex_string)
    
    
def main():

    article_title = "Article Title"
    author_name = "Indrajit Ghosh"
    email = "someone@somewhere.com"
    department = "Stat-Math Unit"
    institute = "Indian Statistical Institute Bangalore"
    country = "India"

    informations = {
        "title": article_title,
        "author": author_name,
        "email": email,
        "dept": department,
        "institute": institute,
        "country": country
    }

    output_directory_path = setup_output_directory()

    create_math_constants_tex(output_directory_path)
    create_structure_tex(informations, output_directory_path)
    create_main_tex(informations, output_directory_path)

    os.chdir(output_directory_path)
    subprocess.run(["python3", str(COMPILE_TEX_LIVES_HERE)])

    os.system('clear')

    print(f"\n\n\t\t::: YOUR TeX WORKING DIRECTORY :::\n\n   {output_directory_path}\n\n")


if __name__ == "__main__":

    main()
