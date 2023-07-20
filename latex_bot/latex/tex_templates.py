# A library of LaTeX templates.
#
# Author: Indrajit Ghosh
#
# Created on: Jul 20, 2023
#

from latex import *
from pathlib import Path


class Author:
    """
    A class representing an Article author

    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    """
    _default_name = "Indrajit Ghosh"
    _default_dept = "Statistics and Mathematics Unit"
    _default_institute = "Indian Statistical Institute"
    _default_addr = [
        "8th Mile, Mysore Road",
        "RVCE Post, Bengaluru",
        "Karnataka - 560 059, India"
    ]

    def __init__(
            self,
            name:str=None,
            department:str=None,
            institute:str=None,
            address:list=None,
            email:str=None,
            current_address:list=None,
            support:str=None
    ):
        self._name = (
            name
            if name is not None
            else self._default_name
        )

        self._dept:str = (
            department
            if department is not None
            else self._default_dept
        )

        self._institute:str = (
            institute
            if institute is not None
            else self._default_institute
        )

        self._addr:list = (
            address
            if address is not None
            else self._default_addr
        )

        _fulladdr = [self._dept, self._institute] + self._addr

        self._amsAddrTeX:str = self._add_texlinebreak_to_list(_fulladdr)

        self._email:str = email
        self._curr_addr:list = current_address

        self._currAddrTeX = (
            self._add_texlinebreak_to_list(self._curr_addr)
            if self._curr_addr is not None
            else None
        )

        self._support = support

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new:str):
        self._name = new

    @property
    def department(self):
        return self._dept
    
    @department.setter
    def department(self, new:str):
        self._dept = new
    
    @property
    def institute(self):
        return self._institute

    @institute.setter
    def institute(self, new:str):
        self._institute = new

    @property
    def address(self):
        return self._addr
    
    @address.setter
    def address(self, new:list):
        self._addr = new

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new:str):
        self._email = new

    @property
    def current_address(self):
        return self._curr_addr
    
    @current_address.setter
    def current_address(self, new:list):
        self._curr_addr = new


    @staticmethod
    def _add_texlinebreak_to_list(lst:list):
        """
        This function accepts a list and add `\\` i.e. r"\textbackslash{}\textbackslash{}"
        in between each elements.

        Parameter(s):
        -------------
            `lst`: `list`

        Returns:
        --------
            `str`

        Example:
        --------
        >>> lst = ["Indrajit Ghosh", "RS Hostel", "ISI Bangalore"]
        >>> _add_texbackslash_to_list(lst)
            r"Indrajit Ghosh\\RS Hostel\\ISI Bangalore"
        """
        fine_lst = []
        for e in lst:
            if e != "":
                fine_lst.append(e)
        
        return "\\\\".join(fine_lst)


class AmsArticle:
    """
    A class representing AMS Aricle LaTeX document.

    Author: Indrajit Ghosh
    Date: Jul 20, 2023

    """
    default_title = "\\AmS-art \\TeX\\ Template"
    default_authors = [Author()]
    default_date = r"\today"
    default_project_dir = Path.cwd() / "new_ams_art"

    TEX_NONE = ['', '  ', '\t']

    def __init__(
            self,
            title:str = None,
            authors:list = None,
            short_title:str = None,
            subjectclass:str = None,
            dedicatory:str = None,
            keywords:str = None,
            date:str = None,
            preamble:str = None,
            sections:list = None,
            project_dir:Path = None,
            *,
            pdfsubject:str = "Mathematics",
            pdfkeywords:str = "Operator Algebras, von-Neumann Algebras",
            pdfcreator:str = "MixTeX",
            pdfcreationdate:str = r"\today",
            pdfcolorlink:bool = True,
            pdflinkcolor:str = "cyan",
            pdfurlcolor:str = "blue",
            pdfcitecolor:str = "magenta",
            papersize:str = "a4paper",
            fontsize:str = "12pt",
            **kwargs
    ):
        self._title:str = (
            title if title is not None
            else self.default_title
        )

        self._authors:list = (
            authors if authors is not None
            else self.default_authors
        )

        self._short_title:str = (
            self._title if short_title is None
            else short_title
        )

        self._subject_class:str = subjectclass
        self._dedicatory:str = dedicatory
        self._keywords:str = keywords
        self._date:str = (
            self.default_date if date is None
            else date
        )
        self._project_dir:Path = (
            self.default_project_dir if project_dir is None
            else Path(project_dir)
        )
        
        # PDF info
        self._pdftitle = title
        self._pdfauthor = ", ".join([ath.name for ath in self._authors])
        self._pdfsubject = pdfsubject
        self._pdfkeywords = pdfkeywords
        self._pdfcreator = pdfcreator
        self._pdfcreationdate = pdfcreationdate
        self._pdfcolorlink = pdfcolorlink
        self._pdflinkcolor = pdflinkcolor
        self._pdfurlcolor = pdfurlcolor
        self._pdfcitecolor = pdfcitecolor
        self._papersize = papersize
        self._fontsize = fontsize

        # Setting up AMS Project components
        self._sections_dir:Path = self._project_dir / "sections"



def main():
    
    p = TexPackage("amsmath")
    print(p)


if __name__ == '__main__':
    main()