# A library of LaTeX templates.
#
# Author: Indrajit Ghosh
# Created on: Jul 20, 2023
#

from latex import *
from pathlib import Path
from datetime import datetime

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`


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

        self._amsAddrTeX:str = self._add_comma_to_list(_fulladdr)

        self._email:str = email
        self._curr_addr:list = current_address

        self._currAddrTeX = (
            self._add_comma_to_list(self._curr_addr)
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

    @property
    def support(self):
        return self._support
    
    @support.setter
    def support(self, new:str):
        self._support = new


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
    
    @staticmethod
    def _add_comma_to_list(lst:list, _and:bool=True):
        """
        This function accepts a list and add `, ` in between each of its elements.

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
            r"Indrajit Ghosh, RS Hostel and ISI Bangalore"
        """
        fine_lst = []
        for e in lst:
            if e != "":
                fine_lst.append(e)

        if not _and:
            return ", ".join(fine_lst)
        
        return ", ".join(fine_lst[:-1]) + " and " + fine_lst[-1]
    
    @staticmethod
    def join_authors(lst_authors:list):
        """
        Joins the list of authors and return appropriate `str`

        Parameter:
        ----------
            `list[Author(), ..., Author()]`

        Returns:
        -------
            `str`
        """
        return ", ".join([ath._name for ath in lst_authors])


class AmsArticle:
    """
    A class representing AMS Aricle LaTeX document.

    Author: Indrajit Ghosh
    Date: Jul 20, 2023

    Parameter(s):
    -------------
        `packages`: `list[TexPackage(), ..., TexPackage()]`
        `sections`: `list[TexFile(), ..., TexFile()]`

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
            packages:list = None, # `list` of `TexPackage`s
            sections:list = None, # `list` of `TexFile`s
            references:list = None, # `list` of reference entries
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

        self._packages:list = (
            packages
            if packages is not None
            else self._default_amsart_packages()
        )

        self._sections:list = (
            sections
            if sections is not None
            else self._default_amsart_sections()
        )

        self._references:list = (
            references
            if references is not None
            else self._default_references()
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
        self._pdftitle = self._title
        self._pdfauthor = Author._add_comma_to_list(
            [ath._name for ath in self._authors]
        )
        self._pdfsubject = pdfsubject
        self._pdfkeywords = pdfkeywords
        self._pdfcreator = pdfcreator
        self._pdfcreationdate = pdfcreationdate
        self._pdfcolorlink = (
            'true' if pdfcolorlink
            else ''
        )
        self._pdflinkcolor = pdflinkcolor
        self._pdfurlcolor = pdfurlcolor
        self._pdfcitecolor = pdfcitecolor
        self._papersize = papersize
        self._fontsize = fontsize

        # Setting up AMS Project components
        self._sections_dir:Path = self._project_dir / "sections"

        # Updating the article:
        # The following function call will create/update `preamble`, 
        # `sections` etc
        self._update()


    def _update(self):
        """
        Updates the `article`. This method should be called
        whenever an attr is set.

        This method calls the following methods:
            self._update_preamble()
            self._update_main_tex()
            self._update_reference_bib()
        """
        self._update_preamble()
        self._update_reference_bib()
        self._update_main_tex()


    def _update_main_tex(self):
        """
        This method will update main `TexFile` for the project
        Updates the `self.main_tex` attr
        """
        authors_outside = authors_inside = ''

        i = 1
        for auth in self._authors:
            auth_out, auth_in = self._get_authors_main_tex_info(
                author = auth,
                _index = i
            )
            authors_outside += auth_out
            authors_inside += auth_in
            i += 1

        main_pre_cmds = (
            r"\newcommand{\Title}{" + self._title + "}%"
            + "\n"
            r"\newcommand{\ShortTitle}{" + self._short_title + "}%"
            + "\n\n"
        )

        main_pre_cmds += r"""
%%--------------------------------------------------------------
%%%	        Author(s) Information
%%--------------------------------------------------------------
"""
        main_pre_cmds += authors_outside + "\n"
        main_pre_cmds += "-"*80 + "\n\n"

        if self._subject_class:
            main_pre_cmds += (
                r"\newcommand{\SubjectClassText}{"
                + self._subject_class
                + "}%"
                + "\n"
            )

        if self._dedicatory:
            main_pre_cmds += (
                r"\newcommand{\Dedicatory}{"
                + self._dedicatory
                + "}%"
                + "\n"
            )

        if self._keywords:
            main_pre_cmds += (
                r"\newcommand{\Keywords}{"
                + self._keywords
                + "}%"
                + "\n"
            )

        main_pre_cmds += r"\newcommand{\Date}{" + self._date + "}%\n"
        main_pre_cmds += r"""
%%--------------------------------------------------------------
%%%	       PDF Constants
%%--------------------------------------------------------------
\newcommand{\pdfLinkColor}{cyan}
\newcommand{\pdfUrlColor}{blue}
\newcommand{\pdfCiteColor}{magenta}
"""
        main_pre_cmds += (
            r"\newcommand{\pdfTitle}{" + self._pdftitle + "}%"
            + "\n"
            r"\newcommand{\pdfAuthor}{" + self._pdfauthor + "}%"
            + "\n"
            + r"\newcommand{\pdfSubject}{" + self._pdfsubject + "}%"
            + "\n"
            + r"\newcommand{\pdfKeywords}{" + self._pdfkeywords + "}%"
            + "\n"
            + r"\newcommand{\pdfCreator}{" + self._pdfcreator + "}%"
            + "\n"
            + r"\newcommand{\pdfCreationDate}{" + self._pdfcreationdate + "}%"
            + "\n"
            + r"\newcommand{\pdfColorLink}{" + self._pdfcolorlink + "}%"
            + "\n"
        )

        main_pre_cmds += "-"*80 + "\n\n"

        self._main_preamble = r"\input{" + self.preamble.filename + "}\n"
        self._main_post_doc_cmds = (
            r"\title[\ShortTitle]{\Title}%"
            + "\n"
            + authors_inside
            + "\n"
            + r"\date{\Date}%"
            + "\n"
        )

        if self._dedicatory:
            self._main_post_doc_cmds += r"\dedicatory{\Dedicatory}%" + "\n"
        if self._subject_class:
            self._main_post_doc_cmds += r"\subjclass{\SubjectClassText}%" + "\n"
        if self._keywords:
            self._main_post_doc_cmds += r"\keywords{\Keywords}%" + "\n"

        self._main_body_text = ""
        if self._sections:
            if 'abstract' in [sec._filename for sec in self._sections]:
                # Abstract is there
                self._main_body_text += r"""
\begin{abstract}
    \label{sec:abstract}
    \input{sections/abstract}
\end{abstract}

"""
            
            for sec in self._sections:
                if not sec._filename == "abstract":
                    self._main_body_text += (
                        r"\section{" + sec._filename.title() + "}%\n"
                        + r"\label{sec:" + sec._filename.replace(' ', '') + "}%\n"
                        + r"\input{" + self._sections_dir.name + "/" + sec._filename
                        + "}%\n\n"
                    )
        else:
            self._main_body_text = r"\lipsum[1-2]"

        
        self._main_body_text += r"""
\medskip
\nocite{*}

\bibliographystyle{amsalpha} % Also use `amsplain`
"""
        self._main_body_text += r"\bibliography{" + self.reference_bib.filename + "}%\n"

        self._main_pre_doc_cmds = main_pre_cmds

        self.main_tex = TexFile(
            tex_compiler="pdflatex",
            output_format=".pdf",
            documentclass= (
                "\\documentclass["
                + self._fontsize + ","
                + self._papersize
                + "]{amsart}%"
            ),
            preamble=self._main_preamble,
            pre_doc_commands=self._main_pre_doc_cmds,
            post_doc_commands=self._main_post_doc_cmds,
            body_text=self._main_body_text,
            file_extension=".tex",
            filename="main",
            classfile=False
        )


    def _update_preamble(self):
        """
        TODO: Add math constants to preamble
        Updates the preamble.
        If at any  moment `self._authors` gets updated this function 
        should be called to update the `self._preamble`.
        """
        # TODO: Adjust `theorem_style` and `custom_commands` attr for preamble
        self.preamble:Preamble = Preamble(
            filename="preamble",
            packages=self._packages,
            author=self._pdfauthor
        )

    def _update_reference_bib(self):
        """
        Updates reference
        """
        _ref_body_text = ""
        for ref in self._references:
            _ref_body_text += ref

        self.reference_bib = TexFile(
            filename="references",
            classfile=True,
            file_extension=".bib",
            body_text=_ref_body_text,
            author=self._pdfauthor
        )

    def add_package(self, package:TexPackage):
        """
        Appends `package` to `self._packages`
        """
        self._packages.append(package)
        self._update()

    def add_reference(self, ref:str):
        """
        Appends `ref` to `self._references`
        """
        self._references.append(ref)
        self._update()

    @staticmethod
    def num_to_word(num:int):
        """
        # TODO: Write it properly
        Converts a given `num` into english words.

        Example:
        --------
        >>> num_to_word(78)
            "seventy eight"

        Reference:
        ----------
            "https://www.javatpoint.com/python-program-to-convert-a-given-number-into-words"
        """
        _ones = {
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5 : "five",
            6 : "six",
            7 : "seven",
            8 : "eight",
            9 : "nine"
        }

        return _ones[num]
    
    @staticmethod
    def _get_authors_main_tex_info(author:Author, _index:int=None):
        """
        Returns:
        --------
         `tuple`: _author_outside_begin_doc, _author_inside_begin_doc

            _author_outside_begin_doc = r'''
                    \newcommand{\AuthorOne}{<AUTHOR>}
                    \newcommand{\AuthorOneAddr}{%
                        <ADDR>
                    }
                    \newcommand{\AuthorOneCurrAddr}{%
                        <CURR_ADDR>
                    }
                    \newcommand{\AuthorOneEmail}{%
                        <EMAIL>
                    }
                    \newcommand{\AuthorOneThanks}{%
                        <THANKS>
                    }
                '''

            _author_inside_begin_doc = r'''
                %  Information for author <_index>
                \author{\Author<_index>}
                \address{\Author<_index>Addr}
                \curraddr{\Author<_index>CurrAddr}
                \email{\Author<_index>Email}
                \thanks{\Author<_index>Thanks}
            '''


        """
        _index = (
            '' if _index is None
            else AmsArticle.num_to_word(_index).title()
        )

        _auth_initial = "\\newcommand{\\" + "Author" + _index 
        _author_outside_begin_doc = (
            "\n"
            + _auth_initial + r"}{" + author.name + r"}"
            + "%\n"
        )

        _author_inside_begin_doc = (
            "\n"
            + f"% Author {_index} information"
            + "\n"
            + r"\author{\Author" + _index + "}%"
            + "\n"
        )

        if author.address:
            _author_outside_begin_doc += (
                _auth_initial + r"Addr}{%"
                + "\n"
                + author._amsAddrTeX
                + "\n"
                + r"}%"
                + "\n"
            )

            _author_inside_begin_doc += (
                f"% Author {_index} address"
                + "\n"
                + r"\address{\Author" + _index + "Addr}%"
                + "\n"
            )

        if author.current_address:
            _author_outside_begin_doc += (
                _auth_initial + r"CurrAddr}{%"
                + "\n"
                + author._currAddrTeX
                + "\n}%"
                + "\n"
            )

            _author_inside_begin_doc += (
                f"% Author {_index} current address"
                + "\n"
                + r"\curraddr{\Author" + _index + "CurrAddr}%"
                + "\n"
            )

        if author.email:
            _author_outside_begin_doc += (
                _auth_initial + r"Email}{%"
                + "\n"
                + author.email
                + "\n}%"
                + "\n"
            )
            
            _author_inside_begin_doc += (
                f"% Author {_index} email"
                + "\n"
                + r"\email{\Author" + _index + "Email}%"
                + "\n"
            )

        if author.support:
            _author_outside_begin_doc += (
                _auth_initial + r"Thanks}{%"
                + "\n"
                + author.support
                + "\n}%"
                + "\n"
            )

            _author_inside_begin_doc += (
                f"% Author {_index} support"
                + "\n"
                + r"\thanks{\Author" + _index + "Thanks}%"
                + "\n"
            )

        return _author_outside_begin_doc, _author_inside_begin_doc


    @staticmethod
    def _default_amsart_packages():
        """
        Returns a `list` of default `TexPackage`s which Indrajit 
        uses for `amsart`

        Returns:
        --------
            `list[TexPackage(), ..., TexPackage()]`
        """
        return [
            TexPackage(
                name="geometry",
                options=[
                    "top=0.9in",
                    "bottom=1in",
                    "left=1in",
                    "right=1in"
                ]
            ),
            TexPackage(
                name=["amsmath", "amssymb", "amsthm"],
                comment= "amssymb internally loads amsfonts"
            ),
            TexPackage(name="inputenc", options=["utf8"]),
            TexPackage(name="mathtools"),
            TexPackage(name="mathrsfs", comment="renders \mathscr cmd"),
            TexPackage(name="xfrac", comment="renders diagonal frac notation: use \\sfrac{}{}"),   
        ]
    

    @staticmethod
    def _default_amsart_sections():
        """
        Returns a `list` of default `TexFile`s which Indrajit 
        uses for `amsart` sections

        Returns:
        --------
            `list[TexFile(), ..., TexFile()]`
        """
        intro = TexFile(
            filename="introduction",
            classfile=True,
            file_extension=".tex",
            body_text=r"""
\lipsum[1-2]
\begin{equation} 
\mathcolor{red}{\sum_{k=0}^n k = 1 + 2 + 3 + \cdots + n = \dfrac{n(n+1)}{2}}
\label{eq_Pn}
\end{equation}
"""
        )

        abstract = TexFile(
            classfile=True,
            filename="abstract",
            body_text=r"\lipsum[1]" + "\n",
            file_extension=".tex"
        )

        sec1 = TexFile(
            filename="section1",
            classfile=True,
            file_extension=".tex",
            body_text=r"""
\lipsum[1-2]
\begin{theorem}
    The set of $\N$ is unbounded.
\end{theorem}
\begin{proof}
    The proof is obvious.
\end{proof}
"""
        )

        sec2 = TexFile(
            filename="section2",
            classfile=True,
            file_extension=".tex",
            body_text=r"\lipsum[1-2]" + "\n"
        )

        return [intro, abstract, sec1, sec2]
    
    
    @staticmethod
    def _default_references():
        """
        Returns:
        --------
            `list[`str`, ..., `str`]`
        """
        ref1 = r"""
@Book{konrad_unbdd,
 Author = {Schm{\"u}dgen, Konrad},
 Title = {Unbounded self-adjoint operators on {Hilbert} space},
 FSeries = {Graduate Texts in Mathematics},
 Series = {Grad. Texts Math.},
 ISSN = {0072-5285},
 Volume = {265},
 ISBN = {978-94-007-4752-4; 978-94-007-4753-1},
 Year = {2012},
 Publisher = {Dordrecht: Springer},
 Language = {English},
 Keywords = {47-01,47B25,81Q10,47Axx,47E05,47F05,35Pxx},
 zbMATH = {6046473},
 Zbl = {1257.47001}
}

"""
        ref2 = r"""
@Article{kaufman,
 Author = {Kaufman, William E.},
 Title = {Representing a closed operator as a quotient of continuous operators},
 FJournal = {Proceedings of the American Mathematical Society},
 Journal = {Proc. Am. Math. Soc.},
 ISSN = {0002-9939},
 Volume = {72},
 Pages = {531--534},
 Year = {1978},
 Language = {English},
 DOI = {10.2307/2042466},
 Keywords = {47A10,47A55},
 zbMATH = {3627811},
 Zbl = {0404.47001}
}

"""
        ref3 = r"""
@Article{lennon,
 Author = {Lennon, M. J. J.},
 Title = {On sums and products of unbounded operators in {Hilbert} space},
 FJournal = {Transactions of the American Mathematical Society},
 Journal = {Trans. Am. Math. Soc.},
 ISSN = {0002-9947},
 Volume = {198},
 Pages = {273--285},
 Year = {1974},
 Language = {English},
 DOI = {10.2307/1996759},
 Keywords = {47A65,47C99},
 zbMATH = {3467887},
 Zbl = {0298.47012}
}
"""
        return [ref1, ref2, ref3]


def main():

    indra = Author(current_address=["Calcutta University", "Kolkata, India"],
                   email="indrajit@gmail.com",
                   support="This paper is supported by ISI"
                   )
    
    article = AmsArticle(
        authors=[
            indra,
            Author(
                name="Soumyashant Nayak",
                email="nsoum@gmail.com",
            )
        ],
        subjectclass="4bdjf, dkfsoi45, 23jJokL",
        dedicatory="This paper is dedicated to my Mother",
        keywords="Mathematics, Operator Algebras"
    )

    print(article.preamble)
    

if __name__ == '__main__':
    main()