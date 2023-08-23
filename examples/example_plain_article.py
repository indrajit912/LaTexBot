# examples/example_plain_article.py
# This script showcases the way one should use the class PlainArticle
#
# Author: Indrajit Ghosh
# Created On: Aug 23, 2023
#
# Run this script from the root_projec_dir using the following cmd
#      `env/bin/python examples/example_plain_article.py`


##################################################################
# The following lines are to set the root_dir to PYTHON path
# And can be ommitted if needed!
##################################################################
import os
import sys

# Get the absolute path of the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path
sys.path.append(parent_dir)
##################################################################

from latex_bot import *

# Create an Author() for the PlainArticle
author1 = Author(
    name="First Lastname",
    department="Stat-Math Unit",
    institute="Indian Statistical Institute",
    address=[
        "8th Mile, Mysore Road",
        "Bangalore 560 059"
    ],
    email="some_one@somewhere.com"
)

# Create the PlainArticle object
article = PlainArticle(
    title="My Cool \\LaTeX\ Article",
    authors=[
        author1
    ],
    project_dir=Path.home() / "Desktop/new_plain_art"
)

# Add some theorem styles
article.add_to_preamble(text=r"\newtheorem{thm}{Theorem}")

# Add some texts
article.add_text(text="\\lipsum[1]")

# Create TexTable
table = TexTable(
    columns=["Name", "Email Id", "Address"]
)

table._rows = [
    ["Indrajit Ghosh", Email("indra_jit@gmail.com", texttt=True), "ISI Bangalore"],
    ["Anirban Pal", Email("ani@isibang.ac.in", texttt=True), "ISI Bangalore"],
    ["Ritvik", Email("ritvik@yahoo.in", texttt=True), "IIT Madras"],
    ["Soumyashant Nayak", Email("soumyashant@somewhere.com", texttt=True), "IISc Bangalore"]
]

# Add the table
article.add_table(tex_table=table)


# Add more stuffs
article.add_paragraph(para="\\lipsum[2-3]")

# Add theorem
thm = TexEnvironment(
    name="thm", 
    content=r"Everything is false if \[ \int f(z) \mathrm{d}z = 0.\]"
)
article.add_texenv(thm)


# Show the output
# print(article)
article.show_output()


# Create the article
# article.create()