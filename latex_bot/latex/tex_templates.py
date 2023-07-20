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
    default_authors = ["Indrajit Ghosh"]

    def __init__(
            self,
            title:str = None,
            authors:list = None,
            addresses:list = None,
            current_addresses:list = None,
            emails:list = None,
            supports:list = None,
            short_title:str = None,
            subjectclass:str = None,
            dedicatory:str = None,
            keywords:str = None,
            date:str = None,
            project_dir:Path = None,
            *,
            pdftitle:str = None,
            pdfauthor:str = None,
            pdfsubject:str = None,
            pdfkeywords:str = None,
            pdfcreator:str = None,
            pdfcreationdate:str = r"\today",
            pdfcolorlink:bool = True,
            pdflinkcolor:str = "cyan",
            pdfurlcolor:str = "blue",
            pdfcitecolor:str = "magenta",
    ):
        pass


def main():
    
    indra = Author()


if __name__ == '__main__':
    main()