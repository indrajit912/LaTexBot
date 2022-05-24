# A script to create a blank ams article template
#
# Author: Indrajit Ghosh
#
# Date: November, 2021
#
# Status: Ongoing...
#

from pathlib import Path
import subprocess, os

from templates.main_tex import main_tex_constants
from templates.structure_tex import AMS_STRUCTURE
from templates.math_constants_tex import MATH_CONSTANTS
from templates.references_bib_tex import REFERENCES
from constants import INDRAJIT


HOME = Path.home()
CWD = Path.cwd()

def setup_output_directory():

    output_directory = CWD / "new_ams_article"
    Path.mkdir(output_directory)
    
    imgs = output_directory / "images"
    Path.mkdir(imgs)

    ref_filename = output_directory / "references.bib"
    with open(ref_filename, "w") as f:
        f.write(REFERENCES)

    return output_directory


def create_math_constants_tex(output_dir):
    print(MATH_CONSTANTS)

    filename = output_dir / "math_constants.tex"
    with open(filename, "w") as f:
        f.write(MATH_CONSTANTS)


def create_structure_tex(output_dir):

    with open(output_dir / "structure.tex", "w") as f:
        f.write(AMS_STRUCTURE)

    print(AMS_STRUCTURE)


def create_main_tex(info:dict, output_dir):

    title = info['title']
    authorname = info['author']
    email = info['email']
    address = info['address']
    INDENT = "    "

    m1, m3, m7 = main_tex_constants
    m2 = INDENT + r"""\title{""" + title + "}\n"
    m4 = INDENT + r"""\author{""" + authorname + "}\n"
    m5 = INDENT + r"""\address{""" + address + "}\n"
    m6 = INDENT + r"""\email{""" + email + "}\n"

    tex_string = m1 + m2 + m3 + m4 + m5 + m6 + m7

    with open(output_dir / "main.tex", "w") as f:
        f.write(tex_string)

    print(tex_string)
    
    
def main():

    article_title = "Your Article's Title Here" # TODO: Take input
    author_name = "Your Name Here"
    email = "someone@somewhere.com"
    address = "Enter your address"

    your_info = {
        "title": article_title,
        "author": author_name,
        "email": email,
        "address": address
    }

    informations = INDRAJIT # Don't forget to update here

    informations.setdefault("title", article_title)

    output_directory_path = setup_output_directory()

    create_math_constants_tex(output_directory_path)
    create_structure_tex(output_directory_path)
    create_main_tex(informations, output_directory_path)


    os.chdir(output_directory_path)
    subprocess.run(["python3", "~/Documents/latex_files/scripts_for_tex/compile_tex.py"])


if __name__ == "__main__":

    main()
