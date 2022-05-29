# Functions needed for `tex_bot`
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
#

from pathlib import Path
import subprocess, os, shutil

from constants import *

from tex_templates.references_bib_tex import REFERENCES
from tex_templates.math_constants_tex import MATH_CONSTANTS
from tex_templates.thesis_style_ist_tex import STYLE_IST
from tex_templates.art_sections_tex import SECTIONS

from tex_templates.ams_structure_tex import AMS_STRUCTURE
from tex_templates.thesis_structure_tex import THESIS_STRUCTURE
from tex_templates.art_structure_tex import ARTICLE_STRUCTURE
from tex_templates.beamer_structure_tex import BEAMER_STRUCTURE

from tex_templates.ams_main_tex import ams_main_tex_constants
from tex_templates.art_main_tex import art_main_tex_constants
from tex_templates.thesis_chapters_tex import *
from tex_templates.thesis_main_tex import MAIN
from tex_templates.beamer_main_tex import BEAMER_MAIN

from tex_templates.beamer_indrametrodrid_sty import INDRAMETRODRID


HOME = Path.home()
CWD = Path.cwd()

IMAGE_FILE = HOME / "Documents/latex_files/scripts_for_tex/latex_bot/tex_templates/latex.jpeg" # Change here accordingly


def choose_from_list(given_list:list, msg_output:str="Choose an option from below"):
    """
    It accepts any list of options: ['open', 'save', 'cancel']
    Ask for a input() among the elements from the list.
    Finally return the `option` user chose!
    """
    print(f"\n{INDENT}{STYLE['subheading']}{msg_output}{STYLE['reset']}")
    for i, el in enumerate(given_list):
        print(f"{INDENT + '  '}{STYLE['number']}{i + 1}{STYLE['reset']}. {el}")
    
    while True:
        n = int(input())
        if n in [x + 1 for x in range(len(given_list))]:
            break
        print(f"{STYLE['error']}KeyError{STYLE['reset']}: Please enter something from the list {[x + 1 for x in range(len(given_list))]}")
        

    print()

    return dict(enumerate(given_list))[n - 1]

    

def setup_output_directory(tex_template:str):

    if tex_template == TEX_TEMPLATES["amsart"]:   

        # Output directory for 'amsart' 
        
        output_directory = CWD / "new_ams_article"
        Path.mkdir(output_directory)

        imgs = output_directory / "images"
        Path.mkdir(imgs)

        ref_filename = output_directory / "references.bib"
        with open(ref_filename, "w") as f:
            f.write(REFERENCES)

    
    if tex_template == TEX_TEMPLATES["newart"]:

        # Output directory for 'newart'

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


    if tex_template == TEX_TEMPLATES["thesis"]:

        # Output directory for 'newthesis'

        output_directory = CWD / "new_thesis"
        Path.mkdir(output_directory)

        imgs = output_directory / "Images"
        Path.mkdir(imgs)

        chapters = output_directory / "Chapters"
        Path.mkdir(chapters)

        shutil.copy(IMAGE_FILE, imgs)

        bib_filename = output_directory / "bibliography.bib"
        with open(bib_filename, "w") as f:
            f.write(REFERENCES)

        style_ist = output_directory / "style.ist"
        with open(style_ist, "w") as f:
            f.write(STYLE_IST)


    if tex_template == TEX_TEMPLATES["beamer"]:

        # Output directory for 'beamer'
        output_directory = CWD / "new_beamer"
        Path.mkdir(output_directory)

        ref_filename = output_directory / "references.bib"
        with open(ref_filename, "w") as f:
            f.write(REFERENCES)


    return output_directory



def create_math_constants_tex(output_dir):

    """
    ::::ALERT::: Not using this function anymore in the project
    """

    print(MATH_CONSTANTS)

    filename = output_dir / "math_constants.tex"
    with open(filename, "w") as f:
        f.write(MATH_CONSTANTS)


def create_indra_metrodrid_sty(output_dir):

    filename = output_dir / "beamerthemeIndraMetrodrid.sty"
    with open(filename, "w") as f:
        f.write(INDRAMETRODRID)


def create_structure_tex(tex_template:str, output_dir):
    """
    ::::ALERT::: Not using this function anymore in the project
    """

    if tex_template == TEX_TEMPLATES["amsart"]:
        structure_file = AMS_STRUCTURE

    if tex_template == TEX_TEMPLATES["newart"]:
        structure_file = ARTICLE_STRUCTURE

    if tex_template == TEX_TEMPLATES["thesis"]:
        structure_file = THESIS_STRUCTURE

    if tex_template == TEX_TEMPLATES["beamer"]:
        create_indra_metrodrid_sty(output_dir) 
        structure_file = BEAMER_STRUCTURE

    
    with open(output_dir / "structure.tex", "w") as f:
        f.write(structure_file)
        
    print(structure_file)



def write_thesis_chapters(output_dir):

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


def write_indrapreamble_sty(tex_template:str, output_dir):

    if tex_template == TEX_TEMPLATES['amsart']:
        structure = AMS_STRUCTURE

    elif tex_template == TEX_TEMPLATES['newart']:
        structure = ARTICLE_STRUCTURE

    elif tex_template == TEX_TEMPLATES['beamer']:
        create_indra_metrodrid_sty(output_dir) # Creating Custom Theme
        structure = BEAMER_STRUCTURE

    elif tex_template == TEX_TEMPLATES['thesis']:
        structure = THESIS_STRUCTURE


    preamble = ""

    initial = r"""

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%	   Preamble for """

    initial += tex_template

    initial += r"""
    %%%%		Author: Indrajit Ghosh
    %%%%  Indian Statistical Institute, Bangalore
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


    \ProvidesPackage{indratexpreamble}


    """

    preamble += initial + structure + MATH_CONSTANTS
    
    filename = output_dir / "indratexpreamble.sty"
    with open(filename, 'w') as f:
        f.write(preamble)



def create_main_tex(tex_template:str, info:dict, output_dir):

    title = info['title']
    authorname = info['author']
    email = info['email']
    address = info['address']
    dept = info['dept']
    institute = info['institute']
    country = info['country']
    

    if tex_template == TEX_TEMPLATES["amsart"]:

        m1, m3, m7 = ams_main_tex_constants
        m2 = INDENT + r"""\title{""" + title + "}\n"
        m4 = INDENT + r"""\author{""" + authorname + "}\n"
        m5 = INDENT + r"""\address{""" + address + "}\n"
        m6 = INDENT + r"""\email{""" + email + "}\n"

        tex_string = m1 + m2 + m3 + m4 + m5 + m6 + m7

        with open(output_dir / "main.tex", "w") as f:
            f.write(tex_string)

        print(tex_string)


    if tex_template == TEX_TEMPLATES["newart"]:

        m1, m4, m6 = art_main_tex_constants
        m2 = r"""\title{""" + title + "}\n"
        m3 = r"""\author[1]{""" + authorname + r"""\thanks{Email: """ + email + "}}\n"
        m5 = r"""\affil[1]{\small{""" + dept + r""", \textcolor{olive}{""" + institute + r"""}}}"""

        tex_string = m1 + m2 + m3 + m4 + m5 + m6

        with open(output_dir / "main.tex", "w") as f:
            f.write(tex_string)

        print(tex_string)


    if tex_template == TEX_TEMPLATES['thesis']:

        write_thesis_chapters(output_dir)
        
        with open(output_dir / "main.tex", "w") as f:
            f.write(MAIN)

        print(MAIN)


    if tex_template == TEX_TEMPLATES['beamer']:

        with open(output_dir / "main.tex", "w") as f:
            f.write(BEAMER_MAIN)

        print(BEAMER_MAIN)