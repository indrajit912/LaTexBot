# This script gives an example of TexFile.render_tex_template() 
#
# Author: Indrajit Ghosh
# Created On: Aug 24, 2023
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

from latex_bot import TexFile

template_path = current_dir + '/spam.tex'
variables = {
    'author': 'John Doe',
    'title': 'My Document Title',
    'date': '2023-08-24'
}

rendered_tex_str:str = TexFile.render_tex_template(
    template_path=template_path,
    variable_dict=variables
)

print(rendered_tex_str)