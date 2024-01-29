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


from latex_bot import Beamer, Frame, BeamerSection
from pathlib import Path

def main():
    pass

if __name__ == '__main__':
    main()
    