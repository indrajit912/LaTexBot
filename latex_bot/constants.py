# Constants needed for `tex_bot`
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
#

from terminal_style import IndraStyle

TEX_TEMPLATES = {
    "newart" : "Plain Article",
    "amsart" : "AMS Article",
    "thesis" : "PhD Thesis",
    "beamer" : "Beamer Presentation",
    "quit" : "Quit the Bot"
}

INDENT = "    "

INDRAJIT = {
    "author": "Indrajit Ghosh",
    "email": "rs\_math1902@isibang.ac.in",
    "address": "Indian Statistical Institute, 8th Mile, Mysore Road, RVCE Post, Bengaluru - 560059, Karnataka, India",
    "dept": "Stat-Math Unit",
    "institute": "Indian Statistical Institute Bangalore",
    "country": "India"
}


STYLE = {

    'className': IndraStyle.AQUA + IndraStyle.ITALLIC,
    'classValue': IndraStyle.PERU,
    'shelfName': IndraStyle.ORANGE + IndraStyle.ITALLIC,
    'libraryName': IndraStyle.NAVAJO_WHITE,
    'symbol': IndraStyle.YELLOW,
    'bracket1': IndraStyle.MAGENTA, # e.g., [, {, &, etc
    'bracket2':IndraStyle.STEEL_BLUE,
    'number': IndraStyle.AQUA_MARINE,
    'id': IndraStyle.SPRING_GREEN,
    'reset': IndraStyle.END,
    'itallic': IndraStyle.ITALLIC,
    'heading': IndraStyle.BOLD + IndraStyle.LIGHT_YELLOW,
    'subheading': IndraStyle.BOLD + IndraStyle.CORAL,
    'value': IndraStyle.ITALLIC + IndraStyle.PALE_GOLDEN_ROD,
    'error': IndraStyle.RED,
    'highlight': IndraStyle.BLINK + IndraStyle.RED + IndraStyle.ITALLIC + IndraStyle.BOLD
}