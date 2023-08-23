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
    email="someone@somewhere.com"
)

# Create the PlainArticle object
article = PlainArticle(
    title="My Cool \\LaTeX Article",
    authors=[
        author1
    ],
    project_dir=Path.home() / "Desktop/new_plain_art"
)

# Show the output
article.show_output()

# Create the article
# article.create()