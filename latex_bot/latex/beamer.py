# A module for Beamer Template.
#
# Author: Indrajit Ghosh
# Created on: Jan 29, 2024
#

from .latex import *

from datetime import datetime
from pathlib import Path
from typing import Union

__all__ = ["Beamer"]


class Beamer:
    """
    A class representing Beamer LaTeX document.

    Author: Indrajit Ghosh
    Date: Jan 29, 2024
    """
    def __init__(
        self,
        title:str=None,
        subtitle:str=None,
        author:str=None,
        institute:str=None,
        institute_code:str=None,
        email:Email=None,
        purpose:str=None,
        date:Union[str, datetime]=None,
        references:list=None,
        project_dir:Path=None,
        *,
        short_title:str=None,
        pdfsubject:str = "Mathematics Presentation",
        pdfcreator:str = "MixTeX",
        pdfcreationdate:str = r"\today",
    ):
        pass