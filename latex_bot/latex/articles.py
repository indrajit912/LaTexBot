# A module for Article Template.
#
# Author: Indrajit Ghosh
# Created on: Jul 20, 2023
#

from .latex import *
from .indrajit_ams_templates import IndraAMS
from .tex_templates import TexFontTemplates
from .utils import compile_tex, open_file

import os, subprocess
from pathlib import Path
from datetime import datetime
from typing import Union

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`
TEX_GARBAGE_DIR = Path(__file__).parent / "tex_garbage"

__all__ = ["PlainArticle", "Article", "AmsArticle"]



class PlainArticle:
    """
    A class representing Plain Article LaTeX document.

    Author: Indrajit Ghosh
    Date: Jul 22, 2023

    This class provides functionality to create a Plain Article in LaTeX format.
    It supports customization of title, authors, date, abstract, body text, and more.
    The class generates the main LaTeX file, compiles it, and can also show the output
    without creating the full project.

    Args:
        `title` (str): Title of the Plain Article.
        `authors` (list): List of authors using the Author class.
        `date` (str): Date of the document.
        `packages` (list): List of TexPackage instances for additional packages.
        `body_text` (str): Body text content of the document.
        `project_dir` (Path): Project directory for the Plain Article.
        `amsartstyle` (bool): Use AMS article style if True.
        `abstract` (str): Abstract content of the document.
        `references` (list): References for the document.
        `tex_template` (TexFile): Template to customize the LaTeX structure.

        `pdfsubject` (str): PDF subject metadata.
        `pdfkeywords` (str): PDF keywords metadata.
        `pdfcreator` (str): PDF creator metadata.
        `pdfcreationdate` (str): PDF creation date metadata.
        `pdfcolorlink` (bool): Enable color links in PDF.
        `pdflinkcolor` (str): Color of internal links in PDF.
        `pdfurlcolor` (str): Color of URLs in PDF.
        `pdfcitecolor` (str): Color of citation links in PDF.
        `papersize` (str): Paper size of the document.
        `fontsize` (str): Font size of the document.

    Methods:
        `add_package`: Add a LaTeX package to the document.
        `add_text`: Add text content to the document.
        `add_paragraph`: Add a paragraph to the document.
        `add_section`: Add a section to the document.
        `add_subsection`: Add a subsection to the document.
        `add_table`: Add a table to the document.
        `create`: Create the Plain Article in the specified project directory.
        `show_output`: Show the output without creating the full project.

    Note:
        The class relies on external modules such as `latex`, `Author`, and `TexFile`.
    """
    default_title = "Plain Article \\TeX\\ Template"
    default_authors = [Author()]
    default_date = r"\today"
    default_abstract = ""
    default_body_text = ""
    default_project_dir = Path.cwd() / "new_plain_art"

    def __init__(
            self,
            title:str=None,
            authors:list=None,
            date:str=None,
            packages:list=None,
            body_text:str=None,
            project_dir:Path=None,
            amsartstyle:bool=False,
            abstract:str=None,
            references:list=None,
            tex_template:TexFile=None,
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
            fontsize:str = "11pt",
            
    ):
        self.INDEX = 1

        self._title:str = (
            title if title is not None
            else self.default_title
        )

        # Manage the case when `authors` is Author() class obj
        if authors is None:
            self._authors = self.default_authors
        elif isinstance(authors, Author):
            self._authors = [authors]
        elif isinstance(authors, list):
            self._authors = authors
        else:
            raise TypeError(
                f"`{self.__class__.__name__}.authors` can be either of type `list` or `Author`\n"
            )

        self._packages:list = (
            packages
            if packages is not None
            else self._get_default_packages()
        )

        self._abstract = (
            abstract
            if abstract
            else self.default_abstract
        )

        self._references = (
            references
            if references
            else []
        )

        # `self._body_text` is important.
        # All elements (e.g. \section, \subsection, \table etc)
        # are to be added (concatenated) with it.
        self._elements = {}
        self._elements[self.INDEX] = (
            body_text
            if body_text is not None
            else self.default_body_text
        )
        self.INDEX += 1

        self._body_text:str = (
            "\n".join([e.__str__() for e in self._elements.values()])
            if self._elements
            else ""
        )

        self._date:str = (
            self.default_date if date is None
            else date
        )

        self._project_dir:Path = (
            self.default_project_dir if project_dir is None
            else Path(project_dir)
        )

        self._amsartstyle = amsartstyle # If true, prints authors addresses at the end of article

        self._tex_template = tex_template

        # PDF info
        self._pdftitle = self._title
        self._pdfauthor = Author._add_comma_to_list(
            [ath.name for ath in self._authors]
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

        # The following variable is used to add stuffs in article
        # preamble. This `list` will be added to self._main_tex's 
        # preamble in the method self._update_main_tex()
        self._post_preamble = []

        self._update_main_tex()


    def __str__(self):
        self._update_main_tex()
        return self._main_tex.__str__()
    
    @property
    def abstract(self):
        return self._abstract

    @abstract.setter
    def abstract(self, new_abstract:str):
        self._abstract = new_abstract
        self._update_main_tex()

    @property
    def references(self):
        return self._references
    
    @references.setter
    def references(self, new_refs:list):
        self._references = new_refs
        self._update_main_tex()

    def add_reference(self, reference:str):
        """
        Adds a reference to the Article.
        This function appends the `reference` to `self._references`
        and then set the new reference.
        """
        self._references.append(reference)
        self._update_main_tex()

    def add_package(self, package:TexPackage):
        """
        Appends `package` to `self._packages`
        """
        self._packages.append(package)
        self._update_main_tex()


    def add_text(self, text:str, noindent=False):
        """
        Adds `text` to `self._elements`
        """
        self._elements[self.INDEX] = (
            "\\noindent " + text
            if noindent
            else text
        )
        self.INDEX += 1
        self._update_main_tex()

    def add_paragraph(self, para:str):
        """
        Adds "\n" + `para` to self._elements
        """
        self._elements[self.INDEX] = "\n" + para + "\n"
        self.INDEX += 1
        self._update_main_tex()

    
    def add_section(self, data:Union[TexSection, dict]):
        """
        Adds a `\section` to the Article._body_text

        Attribute:
        ----------
            `data`: `TexSection` or `dict`
                    e.g. {'heading': "Section Heading", 'content': "Section Content"}
        """
        # If `data` is a `dict` then create a `TexSection`
        section = (
            TexSection(**data)
            if isinstance(data, dict)
            else data
        )
        self._elements[self.INDEX] = section
        self.INDEX += 1
        self._update_main_tex()

    
    def add_subsection(self, heading:str, content:str):
        """
        Adds subsection to the Article
        """
        self._elements[self.INDEX] = (
            "\n"
            + r"\subsection{"
            + heading
            + "}%\n"
            + content
            + "\n"
        )
        self.INDEX += 1
        self._update_main_tex()

    
    def add_table(self, tex_table:TexTable):
        """
        Adds TexTable 
        """
        self._elements[self.INDEX] = tex_table.__str__()
        self.INDEX += 1
        self._update_main_tex()

    
    def add_texenv(self, tex_env:TexEnvironment):
        """
        Adds tex_env
        """
        self._elements[self.INDEX] = tex_env.__str__()
        self.INDEX += 1
        self._update_main_tex()

    def add_to_preamble(self, text:str):
        """
        Adds text to the preamble of the main TeX file.
        """
        self._post_preamble.append(text)
        self._update_main_tex()


    def create(self, _compile:bool=True, **kwargs):
        """
        Creates the PlainArticle in `self._project_dir`
        """
        self._update_main_tex()

        # Creating `self._project_dir`
        if not self._project_dir.exists():
            print("\n\n - Creating the project directory...")
            self._project_dir.mkdir()
        else:
            raise FileExistsError(f"The project directory already exists at `{self._project_dir}`\n")

        print(f" - Writing `{self._main_tex.filename}.{self._main_tex.file_extension}`...")
        self._main_tex.write(
            tex_dir=self._project_dir
        )

        _open_pdf = True

        # Create references
        if self._references:
            _refs = "\n".join(self._references)

            _ref_bib = TexFile(
                classfile=True,
                body_text=_refs,
                filename="references",
                file_extension='.bib',
                author=self._authors
            )

            print(f" - Writing `references.bib`...\n")
            _ref_bib.write(tex_dir=self._project_dir)

            # Change _open_pdf so that the pdf won't be opened after the 
            # first pdflatex compilation
            _open_pdf = False

        if _compile:

            print(f"- Compiling using `{self._main_tex._tex_compiler}`")
            self._main_tex._compile(
                tex_dir=self._project_dir,
                _open = _open_pdf,
                **kwargs
            )

            if self._references:
                # cd self._project_dir
                os.chdir(self._project_dir)

                # Compile main.aux
                print(f"- Compiling using `bibtex`")
                _main_aux = self._main_tex._filename + '.aux'
                # os.system(f"bibtex {_main_aux}")
                subprocess.run(
                    ["bibtex", _main_aux],
                    stdout=subprocess.PIPE,
                    cwd=self._project_dir
                )

                # Compile main.tex
                print(f"- Compiling using `{self._main_tex._tex_compiler}`")
                self._main_tex._compile(
                    tex_dir=self._project_dir,
                    _open = False,
                    **kwargs
                )

                # Compile main.tex
                print(f"- Compiling using `{self._main_tex._tex_compiler}`\n")
                self._main_tex._compile(
                    tex_dir=self._project_dir,
                    _open = True,
                    **kwargs
                )



    def show_output(self):
        """
        This method shows the output without creating the project
        It sets `self._project_dir` to `TEX_GARBAGE`
        """
        if not TEX_GARBAGE_DIR.exists():
            TEX_GARBAGE_DIR.mkdir()

        self._update_main_tex()

        self._main_tex._filename = TexFile.tex_hash(self._main_tex.__str__())
        self._project_dir = TEX_GARBAGE_DIR / self._main_tex.filename

        self._update_main_tex()

        if self._project_dir.exists():
            output = self._project_dir / (self._main_tex._filename + self._main_tex._output_format)
            if output.exists():
                open_file(output)
            else:
                print("No Output file found.\n")
        
        else:
            self.create()


    def _update_main_tex(self):
        """
        Updates the `main.tex`
        """
        _main_preamble = ""
        _main_preamble += sum(pkg for pkg in self._packages)

        # Getting author(s) info
        _auths_outside = _auths_inside = ''

        if self._amsartstyle:
            # AMS art style addresses
            _auths_inside = (
                "\n% Author(s) information:\n"
                + r"\author{\textbf{%"
                + "\n"
            )

            _addresses_cmd = (
                "\n\n"
                + r"\newcommand{\Addresses}{{%" 
                + "\n"
                + "\\bigskip"
                + "\n"
                + "\\footnotesize"
                + "\n"
            )

            _temp_auth_cmd_list = []
            _temp_addrs_cmd_list = []

            i = 1
            for auth in self._authors:
                _auth_out, _ = self._get_authors_main_tex_info(
                    author=auth,
                    _index=i,
                    _ams_style=True
                )

                _auths_outside += _auth_out

                _auth_word = AmsArticle.num_to_word(i).title()
                _temp_auth_cmd_list.append(
                    r"\Author"
                    + _auth_word
                )

                _temp_addrs_append = (
                    r"\textsc{\Author"
                    + _auth_word
                    + "Department"
                    + ", "
                    + r"\Author"
                    + _auth_word
                    + "Institute"
                    + ", "
                    + r"\Author"
                    + _auth_word
                    + "Addr"
                    + r"}\par\nopagebreak"
                    + "\n"
                    + r"\textit{E-mail address}: \texttt{"
                    + r"\Author"
                    + _auth_word
                    + "Email"
                    + "}\n"
                    + "\\medskip"
                    + "\n"
                )
                _temp_addrs_cmd_list.append(_temp_addrs_append)

                i += 1
            
            _tmp = "" # In this we'll concat "\AuthorOne, \AuthorTwo\ and \AuthorThree"

            if len(_temp_auth_cmd_list) == 1:
                _tmp += _temp_auth_cmd_list[0]
            else:
                _tmp = ", ".join(_temp_auth_cmd_list[:-1])
                _tmp += "\\ and " + _temp_auth_cmd_list[-1]

            _temp_addrs = "\n".join(_temp_addrs_cmd_list)
            _addresses_cmd += _temp_addrs + "\n}}%\n"

            _auths_outside += _addresses_cmd

            _auths_inside += _tmp + "\n}}%\n"

        else:
            # If there  are one author the command should be `\affil[]{\AuthorOne}`
            if len(self._authors) == 1:
                _auths_outside, _auths_inside = self._get_authors_main_tex_info(
                    author=self._authors[0]
                )
            else:
                i = 1
                for auth in self._authors:
                    auth_out, auth_in = self._get_authors_main_tex_info(
                        author = auth,
                        _index = i
                    )
                    _auths_outside += auth_out
                    _auths_inside += auth_in
                    i += 1

        _main_pre_doc_cmds = (
            "\n\n"
            + r"\newcommand{\Title}{" + self._title + "}%"
            + "\n"
            + _auths_outside
            + "\n"
            + r"\newcommand{\Date}{" + self._date + "}%"
            + "\n"
        )

        _main_pre_doc_cmds += r"""
%%-------------------------------------------------
%%%	       PDF Constants
%%-------------------------------------------------
\newcommand{\pdfLinkColor}{cyan}
\newcommand{\pdfUrlColor}{blue}
\newcommand{\pdfCiteColor}{magenta}
"""
        _main_pre_doc_cmds += (
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

        _main_post_doc_cmds = (
            r"\title{\Title}%"
            + "\n"
            + _auths_inside
            + "\n"
            + r"\date{\Date}%"
            + "\n"
            + r"\maketitle%"
            + "\n"
            + r"\thispagestyle{empty}%"
            + "\n"

        )

        _abst_tex = fr"""
\begin{{abstract}}
	\noindent  {self._abstract}

	\vspace{{0.95cc}}
	\parbox{{24cc}}{{
        {{\it Keywords and Phrases}}: \pdfKeywords
	}}
\end{{abstract}}
"""
        _abst = (
            ""
            if self._abstract == ''
            else _abst_tex
        )

        self._body_text = "\n".join([self._elements[i].__str__() for i in sorted(self._elements.keys())])
        
        _main_body_text = _abst + self._body_text

        _main_end_text = ""

        if self._references:
            # Add to _main_end_text
            _main_end_text = (
                r"% Bibliography"
                + "%\n"
                + r"\nocite{*}"
                + "%\n"
                + r"\bibliographystyle{plain}"
                + "%\n"
                + r"\bibliography{references}"
                + "%\n\n"
            )

        if self._amsartstyle:
            _main_end_text += "\n\\mbox{}%\n\\vfill%\n\\Addresses%"

        _main_end_text = None if _main_end_text == '' else _main_end_text

        _documentclass = f"\\documentclass[{self._fontsize},{self._papersize}]{{article}}"

        # Setting up `main.tex` TexFile
        
        self._main_tex = TexFile(
            tex_compiler="pdflatex",
            output_format=".pdf",
            documentclass=_documentclass,
            pre_doc_commands=_main_pre_doc_cmds,
            preamble= _main_preamble,
            post_doc_commands=_main_post_doc_cmds,
            body_text=_main_body_text,
            end_text=_main_end_text,
            author=self._pdfauthor,
            filename="main",
            file_extension=".tex",
            classfile=False
        )

        self._main_tex.add_to_preamble("\n".join(self._post_preamble))

        if self._tex_template:
            # If TeX template is given then change self._main_tex accordingly
            self._main_tex.tex_compiler = self._tex_template.tex_compiler
            self._main_tex.output_format = self._tex_template.output_format
            self._main_tex.add_to_preamble(
                self._tex_template.preamble
            )

    @staticmethod
    def _get_authors_main_tex_info(author:Author, _index:int=None, _ams_style:bool=False):
        """
        Returns:
        --------
         `tuple`: _author_outside_begin_doc, _author_inside_begin_doc

            _author_outside_begin_doc = r'''
                    \newcommand{\AuthorOne}{<AUTHOR>}
                    \newcommand{\AuthorOneAddr}{%
                        <ADDR>
                    }
                '''

            _author_inside_begin_doc = r'''
                %  Information for author <_index>
                \author[1]{\textbf{\AuthorOne}}
                \affil[1]{
                    <\AuthorOneAddr>
                }
            '''


        """
        _index_val = (
            '' if _index is None
            else str(_index)
        )
        _index = (
            '' if _index is None
            else AmsArticle.num_to_word(_index).title()
        )

        _auth_initial = "\\newcommand{\\" + "Author" + _index 
        _author_outside_begin_doc = (
            "\n"
            + _auth_initial + r"}{" + author.name + r"}"
            + "%\n"
            + _auth_initial + r"Department}{"
            + author.department + "}%"
            + "\n"
            + _auth_initial + r"Institute}{"
            + author.institute + "}%"
            + "\n"
        )

        if author.address:
            _author_outside_begin_doc += (
                _auth_initial + r"Addr}{%" + "\n"
                + Author._add_comma_to_list(author.address, _and=False) 
                + "\n}%"
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

        if not _ams_style:
            _author_inside_begin_doc = (
                "\n"
                + f"% Author {_index} information"
                + "\n"
                + r"\author[" + _index_val + r"]{\textbf{\Author" + _index + "}}%"
                + "\n"
                + r"\affil[" + _index_val + r"]"
                + r"{\Author" + _index + "Department, "
                + r"\Author" + _index + "Institute"
                + r"\\ "
                + r"\Author" + _index + "Addr"
            )
            if  author.email:
                _author_inside_begin_doc += (
                    r"\\ "
                    + "Email: \\texttt{\\Author" + _index
                    + "Email}"
                )
            
            _author_inside_begin_doc += "}%\n"
        else:
            _author_inside_begin_doc = ''
            

        return _author_outside_begin_doc, _author_inside_begin_doc


    @staticmethod
    def _get_default_packages():
        """
        Returns a list of packages for Plain Article
        """
        return [
            TexPackage(name="inputenc", options=['utf8']),
            TexPackage(name="fontenc", options=['T1']),
            TexPackage(
                name="lmodern",
                comment="To get high quality fonts"
            ),
            TexPackage(
                name=["amsmath", "amssymb", "amsthm", "amscd"],
                comment= "amssymb internally loads amsfonts"
            ),
            TexPackage(
                name="geometry",
                options=["top=1in", "bottom=1in", "left=1in", "right=1in"]
            ),
            TexPackage(name="lipsum"),
            TexPackage(
                name="titling",
                comment="Customizing the title section",
                associated_cmds=[
                    r"\setlength{\droptitle}{-4\baselineskip} % Move the title up",
                    r"\pretitle{\begin{center}\LARGE\bfseries} % Article title formatting",
                    r"\posttitle{\end{center}} % Article title closing formatting",
                    "\n"
                ]
            ),
            TexPackage(
                name="authblk",
                options=["blocks"],
                comment="For Author Titling and affiliating Purpose",
                associated_cmds=[
                    r"\renewcommand\Authfont{\fontsize{11}{11}\selectfont}",
                    r"\renewcommand\Affilfont{\fontsize{10}{10.8}\selectfont}",
                    r"\renewcommand*{\Authsep}{, }",
                    r"\renewcommand*{\Authand}{{\bfseries\ and }}",
                    r"\renewcommand*{\Authands}{{\bfseries\ , and }}",
                    r"\setlength{\affilsep}{1em}",
                    r"\newsavebox\affbox",
                    "\n"
                ]
            ),
            TexPackage(name="longtable"),
            TexPackage(
                name="graphicx",
                comment="Required to include graphics"
            ),
            TexPackage(
                name="array",
                comment="This is required for styling tables"
            ),
            TexPackage(
                name="hyperref",
                associated_cmds=r"""
\hypersetup{
	pdftitle={\pdfTitle},
	pdfauthor={\pdfAuthor},
	pdfsubject={\pdfSubject},
	pdfcreationdate={\pdfCreationDate},
	pdfcreator={\pdfCreator},
	pdfkeywords={\pdfKeywords},
	colorlinks=true,
	linkcolor={cyan},
	%    filecolor=magenta,      
	urlcolor=\pdfUrlColor,
	citecolor=\pdfCiteColor,
	pdfpagemode=UseOutlines,
}
"""
            ),   
        ]
    

class Article:
    # TODO: This class needs to be fixed! Article() doesn't print references
    # after compilation.
    r"""
    A class representing an Article LaTeX document.

    Author: Indrajit Ghosh
    Date: Jul 25, 2023
    
    Attributes:
    -------------
        `packages`: `list[TexPackage(), ..., TexPackage()]`
        `theorem_styles`: str
        `custom_commands`: str
        `sections`: `list[TexFile(), ..., TexFile()]`

    """
    default_title = "Article \\LaTeX\\ Template"
    default_authors = [Author()]
    default_date = r"\today"
    default_bibfile = "references.bib"
    default_project_dir = Path.cwd() / "new_article"


    def __init__(
            self,
            title:str = None,
            authors = None,
            short_title:str = None,
            keywords:str = None,
            date:str = None,
            packages:list = None, # `list` of `TexPackage`s
            theorem_styles:str = None,
            custom_commands:str = None,
            sections:list = None, # `list` of `TexFile`s
            references:list = None, # `list` of reference entries
            bibfile:str=None,
            amsartstyle:bool = False, # If true, prints authors addresses at the end of article
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
            fontsize:str = "11pt",
            **kwargs
    ):
        self._title:str = (
            title if title is not None
            else self.default_title
        )

        # Manage the case when `authors` is Author() class obj
        if authors is None:
            self._authors = self.default_authors
        elif isinstance(authors, Author):
            self._authors = [authors]
        elif isinstance(authors, list):
            self._authors = authors
        else:
            raise TypeError(
                f"`{self.__class__.__name__}.authors` can be either of type `list` or `Author`\n"
            )
        

        self._short_title:str = (
            self._title if short_title is None
            else short_title
        )

        self._packages:list = (
            packages
            if packages is not None
            else self._default_article_packages()
        )

        self._theorem_styles:str = (
            theorem_styles
            if theorem_styles is not None
            else Preamble._default_ams_theorem_styles()
        )

        self._custom_commands:str = (
            custom_commands
            if custom_commands is not None
            else r"\newcommand{\N}{\mathbb{N}}"
        )

        self._sections:list = (
            sections
            if sections is not None
            else Article._default_article_sections()
        )

        self._references:list = (
            references
            if references is not None
            else AmsArticle._default_references()
        )

        self._bibfile:str = (
            bibfile
            if bibfile is not None
            else self.default_bibfile
        )

        self._keywords:str = keywords
        self._date:str = (
            self.default_date if date is None
            else date
        )
        self._project_dir:Path = (
            self.default_project_dir if project_dir is None
            else Path(project_dir)
        )

        self._amsartstyle = amsartstyle # If true, prints authors addresses at the end of article


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

        # Setting up Article Project components
        self._sections_dir:Path = self._project_dir / "sections"

        self._update()

    
    def __str__(self):
        self._update_main_tex()
        return self._main_tex.__str__()

    def create(self, _compile:bool=True):
        """
        Creates the Article
        """
        self._update()

        # Creating `self._project_dir`
        if not self._project_dir.exists():
            print("\n\n - Creating the project directory...")
            self._project_dir.mkdir()
            print(" - Creating `sections` dir ...\n")
            self._sections_dir.mkdir()
        else:
            raise FileExistsError(f"The project directory already exists at `{self._project_dir}`\n")

        # Writing LaTeX files
        print(f" - Writing `{self.preamble.filename}{self.preamble.file_extension}`...")
        self.preamble.write(
            tex_dir=self._project_dir
        )

        print(f" - Writing `{self._main_tex.filename}{self._main_tex.file_extension}`...")
        self._main_tex.write(
            tex_dir=self._project_dir
        )


        print(f" - Writing `{self.reference_bib.filename}{self.reference_bib.file_extension}`...")
        self.reference_bib.write(
            tex_dir=self._project_dir
        )


        print("\n - Writing sections...")

        for sec in self._sections:
            print(f" -- Writing `{sec.filename}{sec.file_extension}`...")
            sec.write(
                tex_dir = self._sections_dir
            )

        print(f"\n\nProject Dir: `{self._project_dir}`\n")

        if _compile:
            _main_tex:Path = self._project_dir / (self._main_tex._filename + self._main_tex._file_extension)

            compile_tex(
                texfile=_main_tex,
                tex_compiler='pdflatex',
                output_format='.pdf'
            )


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

        # Getting author(s) info
        _auths_outside = _auths_inside = ''

        if self._amsartstyle:
            # AMS art style addresses
            _auths_inside = (
                "\n% Author(s) information:\n"
                + r"\author{\textbf{%"
                + "\n"
            )

            _addresses_cmd = (
                "\n\n"
                + r"\newcommand{\Addresses}{{%" 
                + "\n"
                + "\\bigskip"
                + "\n"
                + "\\footnotesize"
                + "\n"
            )

            _temp_auth_cmd_list = []
            _temp_addrs_cmd_list = []

            i = 1
            for auth in self._authors:
                _auth_out, _ = PlainArticle._get_authors_main_tex_info(
                    author=auth,
                    _index=i,
                    _ams_style=True
                )

                _auths_outside += _auth_out

                _auth_word = AmsArticle.num_to_word(i).title()
                _temp_auth_cmd_list.append(
                    r"\Author"
                    + _auth_word
                )

                _temp_addrs_append = (
                    r"\textsc{\Author"
                    + _auth_word
                    + "Department"
                    + ", "
                    + r"\Author"
                    + _auth_word
                    + "Institute"
                    + ", "
                    + r"\Author"
                    + _auth_word
                    + "Addr"
                    + r"}\par\nopagebreak"
                    + "\n"
                    + r"\textit{E-mail address}: \texttt{"
                    + r"\Author"
                    + _auth_word
                    + "Email"
                    + "}\n"
                    + "\\medskip"
                    + "\n"
                )
                _temp_addrs_cmd_list.append(_temp_addrs_append)

                i += 1
            
            _tmp = "" # In this we'll concat "\AuthorOne, \AuthorTwo\ and \AuthorThree"

            if len(_temp_auth_cmd_list) == 1:
                _tmp += _temp_auth_cmd_list[0]
            else:
                _tmp = ", ".join(_temp_auth_cmd_list[:-1])
                _tmp += "\\ and " + _temp_auth_cmd_list[-1]

            _temp_addrs = "\n".join(_temp_addrs_cmd_list)
            _addresses_cmd += _temp_addrs + "\n}}%\n"

            _auths_outside += _addresses_cmd

            _auths_inside += _tmp + "\n}}%\n"

        else:
            # If there  are one author the command should be `\affil[]{\AuthorOne}`
            if len(self._authors) == 1:
                _auths_outside, _auths_inside = PlainArticle._get_authors_main_tex_info(
                    author=self._authors[0]
                )
            else:
                i = 1
                for auth in self._authors:
                    auth_out, auth_in = PlainArticle._get_authors_main_tex_info(
                        author = auth,
                        _index = i
                    )
                    _auths_outside += auth_out
                    _auths_inside += auth_in
                    i += 1

        _main_pre_doc_cmds = (
            "\n\n"
            + r"\newcommand{\Title}{" + self._title + "}%"
            + "\n"
            + r"\newcommand{\ShortTitle}{" + self._short_title + "}%"
            + "\n"
            + _auths_outside
            + "\n"
            + r"\newcommand{\Date}{" + self._date + "}%"
            + "\n"
        )

        _main_pre_doc_cmds += r"""
%%-------------------------------------------------
%%%	       PDF Constants
%%-------------------------------------------------
\newcommand{\pdfLinkColor}{cyan}
\newcommand{\pdfUrlColor}{blue}
\newcommand{\pdfCiteColor}{magenta}
"""
        _main_pre_doc_cmds += (
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
            + r"\newcommand{\bibFile}{"
            + self._bibfile
            + "}%\n\n"
        )

        _main_preamble = r"\input{preamble}"

        _main_post_doc_cmds = (
            r"\title{\Title}%"
            + "\n"
            + _auths_inside
            + "\n"
            + r"\date{\Date}%"
            + "\n"
            + r"\maketitle%"
            + "\n"
            + r"\thispagestyle{empty}%"
            + "\n"

        )

        _main_body_text = ""

        if self._sections:
            _sec_filenames = [sec._filename for sec in self._sections]
            if 'abstract' in _sec_filenames:
                # Abstract is there
                _main_body_text += fr"""
\begin{{abstract}}
    \label{{sec:abstract}}
    \input{{{self._sections_dir.name}/abstract}}
\end{{abstract}}

"""
            if 'introduction' in _sec_filenames:
                # Introduction is there
                _main_body_text += (
                        r"\section{Introduction}%"
                        + "\n"
                        + r"\label{sec:introduction}" + "\n"
                        + r"\input{" + self._sections_dir.name + "/introduction"
                        + "}%\n\n"
                    )
                
            _special_sections = ["abstract", "introduction"]
            for sec in self._sections:
                if not sec._filename in _special_sections:
                    _main_body_text += (
                        r"\section{" + sec._filename.title() + "}%\n"
                        + r"\label{sec:" + sec._filename.replace(' ', '') + "}%\n"
                        + r"\input{" + self._sections_dir.name + "/" + sec._filename
                        + "}%\n\n"
                    )

        else:
            _main_body_text = r"\lipsum[1-2]"


        _main_end_text = (
            r"\nocite{*}"
            + "\n"
            + "\printbibliography[heading=bibintoc,title={References}]"
            + "\n"
        )

        if self._amsartstyle:
            _main_end_text += "\n\n\\mbox{}%\n\\vfill%\n\\Addresses%"

        _documentclass = f"\\documentclass[{self._fontsize},{self._papersize},twoside]{{article}}"

        # Setting up `main.tex` TexFile
        self._main_tex = TexFile(
            tex_compiler="pdflatex",
            output_format=".pdf",
            documentclass=_documentclass,
            pre_doc_commands=_main_pre_doc_cmds,
            preamble= _main_preamble,
            post_doc_commands=_main_post_doc_cmds,
            body_text=_main_body_text,
            end_text=_main_end_text,
            author=self._pdfauthor,
            filename="main",
            file_extension=".tex",
            classfile=False
        )


    def _update_preamble(self):
        """
        Updates the preamble.
        If at any  moment `self._authors` gets updated this function 
        should be called to update the `self._preamble`.
        """
        # Adjust `theorem_style` and `custom_commands` attr for preamble
        self.preamble:Preamble = Preamble(
            filename="preamble",
            packages=self._packages,
            theorem_styles=self._theorem_styles,
            custom_commands=self._custom_commands,
            author=self._pdfauthor,
        )
        self.preamble.add_to_document(
            r"\addbibresource{\bibFile}%"
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
    def _default_article_sections():
        """
        Returns a `list` of default `TexFile`s which I 
        use for `article` sections

        Returns:
        --------
            `list[TexFile(), ..., TexFile()]`
        """
        intro = TexFile(
            filename="introduction",
            classfile=True,
            file_extension=".tex",
            body_text=r"""\lipsum[1]
\begin{thm}
    The set of all natural numbers, $\N$, is unbounded.
\end{thm}
\begin{proof}
    The proof is obvious and left to the reader!
\end{proof}
"""
        )

        abstrat = TexFile(
            filename="abstract",
            classfile=True,
            file_extension=".tex",
            body_text=r"\lipsum[1]"
        )

        sec1 = TexFile(
            filename="section1",
            classfile=True,
            file_extension=".tex",
            body_text=r"""\lipsum[3]
\[
\mathcal L_{\mathcal T}(\vec{\lambda})
= \sum_{(\mathbf{x},\mathbf{s})\in \mathcal T}
    \log P(\mathbf{s}\mid\mathbf{x}) - \sum_{i=1}^m
    \frac{\lambda_i^2}{2\sigma^2}
\]
\lipsum[5]
\[
 z = \overbrace{
   \underbrace{x}_\text{\textcolor{blue}{real}} + i
   \underbrace{y}_\text{imaginary}
  }^\text{\textcolor{red}{complex number}}
\]
"""
        )

        sec2 = TexFile(
            filename="section2",
            classfile=True,
            file_extension=".tex",
            body_text=r"""\lipsum[9]
\[
 \lim_{x\to 0}{\frac{e^x-1}{2x}}
 \overset{\left[\frac{0}{0}\right]}{\underset{\mathrm{H}}{=}}
 \lim_{x\to 0}{\frac{e^x}{2}}={\frac{1}{2}}
\]
\lipsum[6]
Heat Equation:
\[
 \frac{\partial u}{\partial t}
   = h^2 \left( \frac{\partial^2 u}{\partial x^2}
      + \frac{\partial^2 u}{\partial y^2}
      + \frac{\partial^2 u}{\partial z^2} \right) 
\]
\lipsum[10-13]
"""
        )

        return [intro, abstrat, sec1, sec2]


    @staticmethod
    def _default_article_packages():
        """
        Returns LaTeX packages that I usually use in `article` doc.
        """
        return [
            TexPackage(name="inputenc", options=['utf8']),
            TexPackage(name="fontenc", options=['T1']),
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
                name=["amsmath", "amssymb", "amsthm", "amscd"],
                comment= "amssymb internally loads amsfonts"
            ),
            TexPackage(name="xcolor"),
            TexPackage(name="lipsum"),
            TexPackage(
                name="lastpage",
                comment="To get the last page and total number of pages"
            ),
            TexPackage(
                name="babel",
                options=["english"]
            ),
            TexPackage(
                name="titling",
                associated_cmds=[
                    r"\setlength{\droptitle}{-4\baselineskip} % Move the title up",
                    r"\pretitle{\begin{center}\LARGE\bfseries} % Article title formatting",
                    r"\posttitle{\end{center}} % Article title closing formatting"
                ]
            ),
            TexPackage(
                name="authblk",
                options=["blocks"],
                associated_cmds=[
                    r"\renewcommand\Authfont{\fontsize{11}{11}\selectfont}",
                    r"\renewcommand\Affilfont{\fontsize{10}{10.8}\selectfont}%",
                    r"\renewcommand*{\Authsep}{, }",
                    r"\renewcommand*{\Authand}{{\bfseries\ and }}",
                    r"\renewcommand*{\Authands}{{\bfseries\ , and }}",
                    r"\setlength{\affilsep}{1em}",
                    r"\newsavebox\affbox"
                ]
            ),
            TexPackage(
                name="abstract",
                associated_cmds=[
                    r"\renewcommand{\abstractnamefont}{\normalfont\bfseries}",
                    r"\renewcommand{\abstracttextfont}{\normalfont\small\itshape}",
                ]
            ),
            TexPackage(
                name="fancyhdr",
                associated_cmds=[
                    r"\pagestyle{fancy}",
                    r"\fancyhf{}",
                    r"\fancyhead[CO]{\small\scshape\ShortTitle}",
                    r"\fancyhead[CE]{\small\scshape\pdfAuthor}",
                    r"\fancyfoot[R]{\footnotesize Page \ \thepage \ of \pageref{LastPage}}",
                    r"\renewcommand{\headrulewidth}{0.5pt}",
                    r"\renewcommand{\footrulewidth}{0pt}",
                    r"\setlength{\headheight}{13.59999pt}"
                ]
            ),
            TexPackage(
                name="hyperref",
                associated_cmds=[
                    r"""\hypersetup{
	pdftitle={\pdfTitle},
	pdfauthor={\pdfAuthor},
	pdfsubject={\pdfSubject},
	pdfcreationdate={\pdfCreationDate},
	pdfcreator={\pdfCreator},
	pdfkeywords={\pdfKeywords},
	colorlinks=\pdfColorLink,
	linkcolor={\pdfLinkColor},
	%    filecolor=magenta,      
	urlcolor=\pdfUrlColor,
	citecolor=\pdfCiteColor,
	pdfpagemode=UseOutlines,
}%

"""
                ]
            ),
            TexPackage(
                name="csquotes",
                options=["autostyle=true"],
                comment="Required to generate language-dependent quotes in the bibliography",
            ),
            TexPackage(
                name="tocbibind",
                options=["nottoc"],
                comment="To add bibliogrphy to the table of content"
            ),
            TexPackage(
                name="biblatex",
                options=[
                    "style=alphabetic",
                    "sorting=ynt",
                    "backend=bibtex"
                ]
            )
        ]



class AmsArticle:
    r"""
    A class representing AMS Aricle LaTeX document.

    Author: Indrajit Ghosh
    Date: Jul 20, 2023

    Attributes:
    -------------
        `packages`: `list[TexPackage(), ..., TexPackage()]`
        `theorem_styles`: str
        `custom_commands`: str
        `sections`: `list[TexFile(), ..., TexFile()]`

    """
    default_title = "\\AmS-art \\TeX\\ Template"
    default_authors = [Author()]
    default_date = r"\today"
    default_project_dir = Path.cwd() / "new_ams_art"


    def __init__(
            self,
            title:str = None,
            authors = None,
            short_title:str = None,
            subjectclass:str = None,
            dedicatory:str = None,
            keywords:str = None,
            date:str = None,
            packages:list = None, # `list` of `TexPackage`s
            theorem_styles:str = None,
            custom_commands:str = None,
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
            fontsize:str = "11pt",
            **kwargs
    ):
        self._title:str = (
            title if title is not None
            else self.default_title
        )

        # Manage the case when `authors` is Author() class obj
        if authors is None:
            self._authors = self.default_authors
        elif isinstance(authors, Author):
            self._authors = [authors]
        elif isinstance(authors, list):
            self._authors = authors
        else:
            raise TypeError(
                f"`{self.__class__.__name__}.authors` can be either of type `list` or `Author`\n"
            )
        

        self._short_title:str = (
            self._title if short_title is None
            else short_title
        )

        self._packages:list = (
            packages
            if packages is not None
            else Preamble._default_amsart_packages()
        )

        self._theorem_styles:str = (
            theorem_styles
            if theorem_styles is not None
            else Preamble._default_ams_theorem_styles()
        )

        self._custom_commands:str = (
            custom_commands
            if custom_commands is not None
            else Preamble._default_ams_commands()
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


    def __str__(self):
        self._update_main_tex()
        return self._main_tex.__str__()

    def create(self, _compile:bool=True, **kwargs):
        """
        Creates the AMS project.
        """
        self._update()

        # Creating `self._project_dir`
        if not self._project_dir.exists():
            print("\n\n - Creating the project directory...")
            self._project_dir.mkdir()
            print(" - Creating `sections` dir ...\n")
            self._sections_dir.mkdir()
        else:
            raise FileExistsError(f"The project directory already exists at `{self._project_dir}`\n")

        # Writing LaTeX files
        print(f" - Writing `{self.preamble.filename}{self.preamble.file_extension}`...")
        self.preamble.write(
            tex_dir=self._project_dir
        )

        print(f" - Writing `{self._main_tex.filename}{self._main_tex.file_extension}`...")
        self._main_tex.write(
            tex_dir=self._project_dir
        )


        print(f" - Writing `{self.reference_bib.filename}{self.reference_bib.file_extension}`...")
        self.reference_bib.write(
            tex_dir=self._project_dir
        )


        print("\n - Writing sections...")

        for sec in self._sections:
            print(f" -- Writing `{sec.filename}{sec.file_extension}`...")
            sec.write(
                tex_dir = self._sections_dir
            )


        if _compile:
            _main_tex:Path = self._project_dir / 'main.tex'

            compile_tex(
                texfile=_main_tex,
                tex_compiler='pdflatex',
                output_format='.pdf'
            )
        

        print(f"\n\nProject Dir: `{self._project_dir}`\n")



    def _update(self):
        """
        Updates the `article`. This method should be called
        whenever an attr is set.

        This method calls the following methods:
            self._update_preamble()
            self._update_reference_bib()
            self._update_main_tex()
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
            + r"\newcommand{\ShortTitle}{" + self._short_title + "}%"
            + "\n\n"
        )

        main_pre_cmds += r"""
%%--------------------------------------------------------------
%%%	        Author(s) Information
%%--------------------------------------------------------------
"""
        main_pre_cmds += authors_outside + "\n"
        main_pre_cmds += "%" + "-"*80 + "\n\n"

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

        main_pre_cmds += "%" + "-"*80 + "\n\n"

        self._main_preamble = r"\input{" + self.preamble.filename + "}\n"
        self._main_post_doc_cmds = (
            r"\title[\MakeUppercase\ShortTitle]{\MakeUppercase \Title}%"
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

        self._main_body_text = (
            r"\maketitle"
            + "%\n"
            + r"\thispagestyle{empty}"
            + "%\n"
            + r"%\tableofcontents"
            + "\n\n"
        )
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

        self._main_tex = TexFile(
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
        Updates the preamble.
        If at any  moment `self._authors` gets updated this function 
        should be called to update the `self._preamble`.
        """
        # Adjust `theorem_style` and `custom_commands` attr for preamble
        self.preamble:Preamble = Preamble(
            filename="preamble",
            packages=self._packages,
            theorem_styles=self._theorem_styles,
            custom_commands=self._custom_commands,
            author=self._pdfauthor,
        )

    def _update_reference_bib(self):
        """
        Updates references
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
                + r"\address[\Author" + _index + r"]{\Author" + _index + "Addr}%"
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
\begin{thm}
    The set of all natural numbers, $\N$, is unbounded.
\end{thm}
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
@Book{smith_book,
  Author = {Smith, John},
  Title = {Exploring Infinite Operators on {Hilbert} Spaces},
  FSeries = {Graduate Texts in Mathematics},
  Series = {Grad. Texts Math.},
  ISSN = {1234-5678},
  Volume = {123},
  ISBN = {978-12-345-6789-0; 978-98-765-4321-0},
  Year = {2020},
  Publisher = {City Publishers},
  Language = {English},
  Keywords = {Mathematics, Operators, Hilbert Space, Analysis},
  zbMATH = {98765432},
  Zbl = {1234.56789}
}
"""
        ref2 = r"""
@article{smith_2021,
  author    = {Richard A. Doe},
  title     = {Quantum Mechanics in Action},
  journal   = {Journal of Advanced Physics},
  volume    = {42},
  number    = {3},
  pages     = {123--145},
  year      = {2021},
  publisher = {Physics Publishing Co.},
}
"""
        ref3 = r"""
@inproceedings{brown_2020,
  author    = {Michael Brown},
  title     = {Machine Learning Approaches for Image Recognition},
  booktitle = {Proceedings of the International Conference on Computer Science},
  pages     = {56--67},
  year      = {2020},
}
"""
        return [ref1, ref2, ref3]


def main():


    nsoum = Author(
        name="Soumyashant Nayak",
        department="St",
        institute="Indian Statistical Institute Bangalore",
        address=[
            "8th Mile, Mysore Road",
            "Bengaluru 560 059",
            "India"
        ],
        email="soumyashant@gmail.com"
    )

    amsart = AmsArticle(
        authors=[IndraAMS.indrajit, nsoum],
        keywords="von-Neumann Algebras, Affiliated Operators",
        project_dir=Path.home() / "Desktop" / "new_ams_art",
    )

    plainart = PlainArticle(
        authors=IndraAMS.indrajit,
        project_dir=Path.home() / "Desktop" / "new_plain_art",
        amsartstyle=True,
        body_text=""
    )

    art = Article(
        authors=[IndraAMS.indrajit, nsoum],
        project_dir=Path.home() / "Desktop" / "new_article",
        amsartstyle=True,
    )



if __name__ == '__main__':
    main()