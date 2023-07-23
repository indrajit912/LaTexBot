# A module for LaTeX
#
# Author: Indrajit Ghosh
# Date: Jun 17, 2023
#

from datetime import datetime
import copy, re, tempfile
from pathlib import Path

__all__ = ["TexFile", "TexPackage", "Preamble"]

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`


class TexPackage:
    """
    A class to represent a `LaTeX` Package

    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    """
    def __init__(
            self, 
            name, 
            options:list=None,
            comment:str=None,
            associated_cmds:list=None
    ):
        
        if isinstance(name, str):
            self._name = name
        elif isinstance(name, list):
            self._name = ",".join(name)
        else:
            raise TypeError(
                f"The `name` attr of an {self.__class__.__name__} object \ can be of type `str` or `list`.\n"
            )
        
        self._options = (
            ",".join(options) 
            if options is not None
            else ""
        )
        self._comment = (
            comment
            if comment
            else ""
        )
        if associated_cmds is not None:
            if isinstance(associated_cmds, str):
                associated_cmds = [associated_cmds]
            if isinstance(associated_cmds, list):
                pass
            else:
                raise Exception("The attr `associated_cmds` of a `TexPackage` should be of type `list`.")
            
        self._associated_cmds = (
            "%\n".join(associated_cmds)
            if associated_cmds is not None
            else ""
        )


    def __str__(self):
        _pkg_str = ''

        if self._options == '':
            _pkg_str += r"\usepackage{" + self._name + r"}" + f"% {self._comment}\n"
        else:
            _pkg_str += r"\usepackage[" + self._options + r"]{" + self._name + r"}" + f"% {self._comment}\n"

        _pkg_str += self._associated_cmds

        return _pkg_str

    
    def __add__(self, right):
        return self.__str__() + right.__str__()
    
    def __radd__(self, left):
        if left == 0:
            return self
        if isinstance(left, str):
            return left.rstrip().__add__("\n" + self.__str__())
        


class TexFile:
    """
    TeX templates used to create `plainarticle`, `article`, `amsarticle` etc

    Parameters
    ----------
    tex_compiler : :class:`str`
        The TeX compiler to be used, e.g. ``latex``, ``pdflatex`` or ``lualatex``

    output_format : :class:`str`
        The output format resulting from compilation, e.g. ``.dvi`` or ``.pdf``

    documentclass : :class:`str`
        The command defining the documentclass, e.g. ``\\documentclass[11pt,a4paper]{amsart}``

    pre_doc_commands : :class:`str`
        Text to be inserted at the very begining of the file, 
        e.g. ``\\newcommand{\Author}{Indrajit Ghosh}``

    preamble : :class:`str`
        The document's preamble, i.e. the part between ``\\documentclass`` and ``\\begin{document}``

    post_doc_commands : :class:`str`
        Text (definitions, commands) to be inserted at right after ``\\begin{document}``, 
        e.g. ``\\maketitle``

    body_text : :class:`str`
        Texts in between `post_doc_commands` and `end_text`
        e.g. "This is my first LaTeX document."

    end_text : :class:`str`
        This is mainly for `bibliography` related texts (in any) in the TeX file
        This text is added just before "\\end{document}"

    file_extension : :class:`str`
        File extension, e.g. `.tex`, `.bib`, `.sty` etc

    filename : :class: `str`
        Name of the TeX file, e.g. `main`, `bibliography` etc

    author : :class: `str`
        Author of the TexFile

    classfile : :class: `bool`
        If this is true then the TexFile will be assumed to be a class file like `sty`, `cls` etc.
        In `True` case the above attributes will be '' and `body_text` can be updated.
    """

    default_tex_compiler = "pdflatex"
    default_output_format = ".pdf"

    default_documentclass = r"\documentclass[12pt, twoside]{article}"
    default_pre_doc_commands = "\\newcommand{\\Title}{A \\LaTeX file}%\n" + \
                                "\\newcommand{\\Author}{Indrajit Ghosh}%\n"
    default_preamble = r"""
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
"""
    default_post_doc_commands = "\\maketitle"
    default_body_text = "\nYourTextHere\n"
    default_end_text = ""

    default_filename = "untitled"                                     
    default_file_extension = ".tex"
    default_author = "Indrajit Ghosh"


    def __init__(
            self,
            tex_compiler:str=None,
            output_format:str=None,
            documentclass:str=None,
            pre_doc_commands:str=None,
            preamble:str=None,
            post_doc_commands:str=None,
            body_text:str=None,
            end_text:str=None,
            filename:str=None,
            file_extension:str=None,
            author:str=None,
            classfile:bool=False,
    ):
        self._tex_compiler = (
            tex_compiler
            if tex_compiler is not None
            else TexFile.default_tex_compiler
        )

        self._output_format = (
            output_format
            if output_format is not None
            else TexFile.default_output_format
        )

        self._documentclass = (
            documentclass
            if documentclass is not None
            else TexFile.default_documentclass
        )

        self._pre_doc_commands = (
            pre_doc_commands
            if pre_doc_commands is not None
            else TexFile.default_pre_doc_commands
        )

        self._preamble = (
            preamble
            if preamble is not None
            else TexFile.default_preamble
        )

        self._post_doc_commands = (
            post_doc_commands
            if post_doc_commands is not None
            else TexFile.default_post_doc_commands
        )

        self._body_text = (
            body_text
            if body_text is not None
            else TexFile.default_body_text
        )

        self._end_text = (
            end_text
            if end_text is not None
            else TexFile.default_end_text
        )

        self._filename = (
            filename
            if filename is not None
            else TexFile.default_filename
        )

        self._file_extension = (
            file_extension
            if file_extension is not None
            else TexFile.default_file_extension
        )

        self._author = (
            author
            if author is not None
            else TexFile.default_author
        )

        self._classfile = classfile

        if self._classfile:
            self._documentclass = self._preamble = self._post_doc_commands = \
                self._pre_doc_commands = self._output_format = self._end_text = ''

        self._rebuild()

    def _rebuild(self):
        """
        Rebuilds the entire TeX template text from ``\\documentclass`` to 
        ``\\end{document}`` according to all settings and choices.
        """

        _fileinfo = [
            f"{self._filename}{self._file_extension}",
            f"Author(s): {self._author}",
            f"Date: {TODAY}"
        ]
        
        self._fileinfo = self._add_dotted_lines(
            heading=_fileinfo,
            symbol="%"
        )
        
        self.body = self._fileinfo
        # TODO: Add ---- for every parts of the doc
        if not self._classfile:
            self.body += (
                "\n"
                + self._documentclass
                + "%\n%\n"
                + self._pre_doc_commands
                +"%\n"
                + self._preamble
                + "%\n%\n"
                + r"\begin{document}"
                + "%\n"
                + "%\n"
                + self._post_doc_commands
                + "%\n"
                + self._body_text
                + "%\n\n"
                + self._end_text
                + "\n\n"
                + r"\end{document}"
                + "%\n"
            )
        else:
            self.body += self._body_text + "%\n\n"

        self.body += self._add_dotted_lines(
            heading=f"End of `{self._filename}{self._file_extension}`",
            symbol="%"
        )

    @staticmethod
    def _add_dotted_lines(
        heading:str, msg:str=None, symbol:str="%", factor:int=80, _tex=True
    ):
        """
        This function returns lines to the `msg`

        Attributes:
        -----------
            `heading`: `list` or `str`
            `msg` : `str` : Optional
        
        Example
        --------
        >>> TexFile._add_dotted_lines(msg="Here is Text", heading="Hello World!)

                %--------------------------------------------%
                %                Hello World!     # heading           
                %--------------------------------------------%

                Here is Text # msg

                %--------------------------------------------%
        """
        _factor = factor
        _line = "%" + str(symbol) * _factor + "%"
        _tex_symbol = "%" if _tex else ''

        if isinstance(heading, list):
            heading = "\n%".join([el.center(_factor) for el in heading])

        _head = (
            "\n"
            + _line
            + "\n"
            + _tex_symbol + heading.center(_factor)
            + "\n"
            + _line
        )
        if msg is not None:
            _tail = (
                "\n\n"
                + msg
                + "\n\n"
                + _line
                + "\n"
            )

            return _head + _tail + "\n"
        
        return _head + "\n"


    def __str__(self):
        return self.body
    
    def __repr__(self):
        classname = self.__class__.__name__
        return f"{classname}({self._documentclass})"
    
    @property
    def metadata(self):
        return {
            "tex_compiler": self._tex_compiler,
            "output_format": self._output_format,
            "documentclass": self._documentclass,
            "pre_doc_commands": self._pre_doc_commands,
            "preamble": self._preamble,
            "post_doc_commands": self._post_doc_commands,
            "body_text": self._body_text,
            "file_extension": self._file_extension,
            "filename": self._filename,
            "author": self._author
        }
    
    @metadata.setter
    def metadata(self, newdata:dict):
        if 'tex_compiler' in newdata.keys():
            self._tex_compiler = newdata['tex_compiler']
        
        if 'output_format' in newdata.keys():
            self._output_format = newdata['output_format']

        if 'documentclass' in newdata.keys():
            self._documentclass = newdata['documentclass']
        
        if 'preamble' in newdata.keys():
            self._preamble = newdata['preamble']
        
        if 'body_text' in newdata.keys():
            self._body_text = newdata['body_text']
        
        if 'pre_doc_commands' in newdata.keys():
            self._pre_doc_commands = newdata['pre_doc_commands']
        
        if 'post_doc_commands' in newdata.keys():
            self._post_doc_commands = newdata['post_doc_commands']
        
        if 'file_extension' in newdata.keys():
            self._file_extension = newdata['file_extension']

        if 'filename' in newdata.keys():
            self._filename = newdata['filename']
        
        if 'author' in newdata.keys():
            self._author = newdata['author']

        self._rebuild()
    
    def add_to_preamble(self, txt, prepend=False):
        """
        Adds stuff to the TeX template's preamble (e.g. definitions, packages). 
        Text can be inserted at the beginning or at the end of the preamble.

        Parameters
        ----------
        txt : :class:`string`
            String containing the text to be added, e.g. ``\\usepackage{hyperref}``
        prepend : Optional[:class:`bool`], optional
            Whether the text should be added at the beginning of the preamble, i.e. 
            right after ``\\documentclass``. Default is to add it at the end of the 
            preamble, i.e. right before ``\\begin{document}``
        """
        if prepend:
            self._preamble = "\n" + txt + "\n" + self._preamble
        else:
            self._preamble += "\n" + txt + "\n"
        self._rebuild()

    
    def add_to_document(self, txt):
        """Adds txt to the TeX template just after \\begin{document}, e.g. ``\\boldmath``

        Parameters
        ----------
        txt : :class:`str`
            String containing the text to be added.
        """
        self._body_text += "\n" + txt + "\n"
        self._rebuild()


    @property
    def tex_complier(self):
        return self._tex_compiler
    
    @tex_complier.setter
    def tex_compiler(self, compiler:str):
        self._tex_compiler = compiler
        self._rebuild()

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, new_format:str):
        self._output_format = new_format
        self._output_format()

    @property
    def documentclass(self):
        return self._documentclass

    @documentclass.setter
    def documentclass(self, newclass:str):
        self._documentclass = newclass
        self._rebuild()

    @property
    def preamble(self):
        return self._preamble
    
    @preamble.setter
    def preamble(self, newpreamble:str):
        self._preamble = newpreamble
        self._rebuild()

    @property
    def body_text(self):
        return self._body_text
    
    @body_text.setter
    def body_text(self, newtext:str):
        self._body_text = newtext
        self._rebuild()

    @property
    def pre_doc_commands(self):
        return self._pre_doc_commands

    @pre_doc_commands.setter
    def pre_doc_commands(self, newcmds:str):
        self._pre_doc_commands = newcmds
        self._rebuild()

    @property
    def post_doc_commands(self):
        return self._post_doc_commands
    
    @post_doc_commands.setter
    def post_doc_commands(self, newcmds:str):
        self._post_doc_commands = newcmds
        self._rebuild()

    @property
    def file_extension(self):
        return self._file_extension
    
    @file_extension.setter
    def file_extension(self, newext:str):
        if not newext.startswith('.'):
            newext = "." + newext
        self._file_extension = newext
        self._rebuild()

    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, newname:str):
        # If the `newname` ends with an extension then strip it
        self._filename = newname.split('.')[0]
        self._rebuild()

    @property
    def classfile(self):
        return self._classfile
    
    @classfile.setter
    def classfile(self, new:bool):
        self._classfile = new
        self._rebuild()


    def copy(self):
        return copy.deepcopy(self)
    
    def write(self, tex_dir:Path):
        """
        Writes the TexFile() into the given directory `tex_dir`
        and returns the TeX file path

        Parameter:
        ----------
        `tex_dir`: `Path`
                  The directory where to create the TeX file
        Returns:
        --------
        TeX file path: `Path`
        """
        texfilepath = Path(tex_dir) / (self.filename + self.file_extension)
        with open(texfilepath, 'w') as f:
            f.write(self.body)

        return texfilepath
    
    @staticmethod
    def latex_escape(text:str):
        """
        This function accepts plain text and return the TeX escaped text.

        Parameter:
        ----------
            `text`: `str`, a plain text message; This msg should not be any 
                            standard LaTeX command such as `\begin{document}`.
        
        Returns:
        --------
            `str`; the message escaped to paste it into a `.tex` file
        """
        tex_conversion = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
            '<': r'\textless{}',
            '>': r'\textgreater{}',
        }

        regex = re.compile(
            '|'.join(
                re.escape(str(key)) for key in sorted(
                    tex_conversion.keys(), key=lambda item : -len(item)
                )
            )
        )

        return regex.sub(
            lambda match: tex_conversion[match.group()], text
        )
    
    def _compile(self, tex_dir:Path):
        """
        TODO: This function tries to compile the TexFile inside the `_tmp_path`
        """
        # Create `_tmp_path`
        # _tmp_path = tempfile.mkdtemp(prefix="latexbot-tmp.")

        # Write the TexFile inside the _tmp_path
        # self.write(tex_dir=_tmp_path)

        # print(_tmp_path)


class Preamble(TexFile):
    """
    TODO: Improve this class
    A class representing a `TeX` preamble
    This is a `TexFile(classfile=True)` object

    Author: Indrajit Ghosh
    Date: Jul 21, 2023

    Parameter(s):
    -------------
        `packages` : `list[Package(), ..., Package()]`
        `theorem_styles` : `str`
        `custom_commands`: `str`
    """
    def __init__(
            self, 
            packages:list=None,
            theorem_styles:str=None,
            custom_commands:str=None,
            filename:str=None, 
            **kwargs
    ):

        _filename = (
            "preamble" if filename is None
            else filename
        )

        _packages:list = (
            packages if packages is not None
            else self._default_amsart_packages()
        )

        _thm_styles = (
            theorem_styles if theorem_styles is not None
            else self._default_ams_theorem_styles()
        )

        _cmds = (
            custom_commands if custom_commands is not None
            else self._default_ams_commands()
        )

        _preamble_body_text = r"""

%%-----------------------------------------------------------------
%%		Packages for the project
%%-----------------------------------------------------------------

"""
        _preamble_body_text += sum(_packages) + "\n" + "%" + "-"*70

        _preamble_body_text += r"""

%%-----------------------------------------------------------------
%%		Theorem and Environment Styles
%%-----------------------------------------------------------------

"""
        _preamble_body_text += _thm_styles + "\n" + "%" + "-"*70

        _preamble_body_text += r"""

%%-----------------------------------------------------------------
%%		Custom commands and macros
%%-----------------------------------------------------------------

"""
        _preamble_body_text += _cmds + "\n" + "%" + "-"*70

        super().__init__(
            tex_compiler='',
            output_format='.tex',
            classfile=True,
            body_text=_preamble_body_text,
            filename=_filename,
            **kwargs
        )

    @staticmethod
    def _default_amsart_packages():
        """
        Returns LaTeX packages that I usually use in `amsart` doc.
        """
        return [
            TexPackage(name="inputenc", options=['utf8']),
            TexPackage(name="fontenc", options=['T1']),
            TexPackage(
                name="lmodern",
                comment="To get high quality fonts"
            ),
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
}"""
            ]
        ),
        TexPackage(name="xcolor"),
        TexPackage(name="lipsum"),
        ]
    
    @staticmethod
    def _default_ams_theorem_styles():
        """
        Returns ams theorem style that I usually use.
        """
        return r"""

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{prop}[theorem]{Proposition}
\newtheorem{lem}[theorem]{Lemma}
\newtheorem{cor}[theorem]{Corollary}
\newtheorem{notation}[theorem]{Notation}
\renewcommand\qedsymbol{$\blacksquare$}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{xca}[theorem]{Exercise}

\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

\numberwithin{equation}{section}

"""
    
    @staticmethod
    def _default_ams_commands():
        """
        Commands that I usually use in my documents
        """
        return r"""
% Here I define a macro \mathcolor for coloring text in math mode.
\makeatletter
\def\mathcolor#1#{\@mathcolor{#1}}
\def\@mathcolor#1#2#3{%
	\protect\leavevmode
	\begingroup
	\color#1{#2}#3%
	\endgroup
}
\makeatother

% Celling and Floor function
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Operations
\newcommand{\N}{\mathbb{N}}
\newcommand{\quotes}[1]{\textquotedblleft #1\textquotedblright}
"""



def main():
    file = TexFile(end_text="This is the end text")
    print(file)


if __name__ == '__main__':
    main()