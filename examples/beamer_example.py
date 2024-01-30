# examples/beamer_example.py
# This script showcases the way one should use the class Beamer
#
# Author: Indrajit Ghosh
# Created On: Jan 29, 2024
#

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


from latex_bot import Beamer
from pathlib import Path

def main():
    beamer = Beamer(
        title="Sample Presentation",
        subtitle="Here is subtitle",
        author="Indrajit Ghosh",
        institute="Indian Statistical Institute Bangalore",
        email="rs_math1902@isibang.ac.in",
        institute_code="ISI",
        purpose="Write the Conference Name -- Mmm YYYY",
        project_dir=Path.home() / "Desktop/new_beamer"
    )

    beamer.show_output()

if __name__ == '__main__':
    main()
    