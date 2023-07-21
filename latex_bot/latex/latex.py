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
            comment:str=None
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


    def __str__(self):
        if self._options == '':
            return r"\usepackage{" + self._name + r"}" + f"% {self._comment}\n"
        else:
            return r"\usepackage[" + self._options + r"]{" + self._name + r"}" + f"% {self._comment}\n"
    
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
        The command defining the documentclass, e.g. ``\\documentclass[preview]{standalone}``
    preamble : :class:`str`
        The document's preamble, i.e. the part between ``\\documentclass`` and ``\\begin{document}``
    body_text : :class:`str`
        Text in between ``\\begin{document}`` and ``\\end{document}``
    pre_doc_commands : :class:`str`
        Text to be inserted at the very begining of the file, e.g. ``\\newcommand{\Author}{Indrajit Ghosh}``
    post_doc_commands : :class:`str`
        Text (definitions, commands) to be inserted at right after ``\\begin{document}``, e.g. ``\\boldmath``
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

    default_documentclass = r"\documentclass[12pt, twoside]{article}"
    default_preamble = r"""
\usepackage[english]{babel}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
"""
    default_body_text = "\nYourTextHere\n"
    default_tex_compiler = "pdflatex"
    default_output_format = ".pdf"
    default_pre_doc_commands = "\\date{\\today} % keep \\date{} for no date\n" + \
                                            "\\newcommand{\\Author}{Indrajit Ghosh}\n"
                                            
    default_post_doc_commands = ""
    default_file_extension = ".tex"
    default_filename = "untitled"
    default_author = "Indrajit Ghosh"


    def __init__(
            self,
            tex_compiler:str=None,
            output_format:str=None,
            documentclass:str=None,
            preamble:str=None,
            body_text:str=None,
            pre_doc_commands:str=None,
            post_doc_commands:str=None,
            file_extension:str=None,
            filename:str=None,
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

        self._preamble = (
            preamble
            if preamble is not None
            else TexFile.default_preamble
        )

        self._body_text = (
            body_text
            if body_text is not None
            else TexFile.default_body_text
        )

        self._pre_doc_commands = (
            pre_doc_commands
            if pre_doc_commands is not None
            else TexFile.default_pre_doc_commands
        )

        self._post_doc_commands = (
            post_doc_commands
            if post_doc_commands is not None
            else TexFile.default_post_doc_commands
        )

        self._file_extension = (
            file_extension
            if file_extension is not None
            else TexFile.default_file_extension
        )

        self._filename = (
            filename
            if filename is not None
            else TexFile.default_filename
        )

        self._author = (
            author
            if author is not None
            else TexFile.default_author
        )

        self._classfile = classfile

        if self._classfile:
            self._documentclass = self._preamble = self._post_doc_commands = \
                            self._pre_doc_commands = self._output_format = ''

        self._rebuild()

    def _rebuild(self):
        """
        Rebuilds the entire TeX template text from ``\\documentclass`` to 
        ``\\end{document}`` according to all settings and choices.
        """

        self._fileinfo = "\n" + "%"*60 + f"\n%\t{self._filename}{self._file_extension}\n" + \
                                f"%\tAuthor(s): {self._author}\n" + \
                                f"%\tDate: {TODAY}\n" + "%"*60 + "\n\n"
        
        self.body = self._fileinfo
        
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
                + "\n\n"
                + r"\end{document}"
                + "%\n"
            )
        else:
            self.body += self._body_text + "%\n\n"

        self.body += (
            "\n"
            + "%" * 60 + "\n"
            + f"%\t\tEnd of `{self._filename}{self._file_extension}`\n"
            + "%" * 60 + "\n"
        )


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
            "preamble": self._preamble,
            "body_text": self._body_text,
            "pre_doc_commands": self._pre_doc_commands,
            "post_doc_commands": self._post_doc_commands,
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
        self._post_doc_commands += "\n" + txt + "\n"
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
        _preamble_body_text += sum(_packages) + "\n" + "-"*70

        _preamble_body_text += r"""

%%-----------------------------------------------------------------
%%		Theorem and Environment Styles
%%-----------------------------------------------------------------

"""
        _preamble_body_text += _thm_styles + "\n" + "-"*70

        _preamble_body_text += r"""

%%-----------------------------------------------------------------
%%		Custom commands and macros
%%-----------------------------------------------------------------

"""
        _preamble_body_text += _cmds + "\n" + "-"*70


        # TODO: Create the `body_text` for the preamble
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

%\newtheorem{conj}[thm]{Conjecture} 

%%% 
%%% The following gives definition type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{example}[theorem]{Example}
\newtheorem{xca}[theorem]{Exercise}

%%% 
%%% The following gives remark type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}

%%%
%%% The following, if uncommented, numbers equations within sections.
\numberwithin{equation}{section}

%%
%%% My custom theorem styles
%%

\newtheoremstyle{ser}% name
{8pt}% Space above
{8pt}% Space below
{\it}% Body font
{}% Indent amount
{\sf}% Theorem head font
{:}% Punctuation after theorem head
{6mm}% Space after theorem head
{}% Theorem head spec (can be left empty, meaning `normal')

\theoremstyle{ser}
\newtheorem{claim}{Claim}


\newtheoremstyle{serr}% name
{8pt}% Space above
{8pt}% Space below
{\normalfont}% Body font
{}% Indent amount
{\sf}% Theorem head font
{.}% Punctuation after theorem head
{6mm}% Space after theorem head
{}% Theorem head spec (can be left empty, meaning `normal')

\theoremstyle{serr}
\newtheorem{pf_of_claim}{Proof of Claim}

\theoremstyle{ser}
\newtheorem{conj}{Conjecture}

\theoremstyle{ser}
\newtheorem{qn}{Question}

%%
%%% My Custom Environments
%%
%\newenvironment{nam}[args]{begdef}{enddef}
\newenvironment{solution}{\begin{proof}[Solution]}{\end{proof}}

"""
    
    @staticmethod
    def _default_ams_commands():
        """
        Commands that I usually use in my documents
        """
        return r"""
%Sets line spacing to 1 and a half
%\linespread{1.1}

% Color constants : usages- \textcolor{<colorName>}{<text>}
\definecolor{indraRed}{rgb}{0.593, 0.183, 0.183}
\definecolor{indraPink}{rgb}{0.858, 0.188, 0.478}
\definecolor{indraBlue}{rgb}{0, 0.199, 0.398}
\definecolor{madridBlue}{rgb}{0.199, 0.199, 0.695}
\definecolor{metropolisThemeColor}{rgb}{0.105, 0.214, 0.234}
\definecolor{metropolisBarColor}{rgb}{0.984, 0.0.515, 0.015}
\definecolor{UBCblue}{rgb}{0.04706, 0.13725, 0.26667} % UBC Blue (primary)
\definecolor{UBCgrey}{rgb}{0.3686, 0.5255, 0.6235} % UBC Grey (secondary)

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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%----------------------------------------------------
%%		 Math Constants
%%-----------------------------------------------------

%%%%%% Basic Set Theory %%%%%%%%%%%%
\newcommand{\ra}{\rightarrow} % right arrow


%%%%%% Calculus Symbols %%%%%%%%%%%%
\newcommand{\cvec}[1]{{\mathbf #1}} % bold R^n vector
\newcommand{\rvec}[1]{\vec{\mathbf #1}} % vector with arrow
\newcommand{\ihat}{\hat{\textbf{\i}}}
\newcommand{\jhat}{\hat{\textbf{\j}}}
\newcommand{\khat}{\hat{\textbf{k}}}
\newcommand{\mdiv}{{\rm div}} % divergence
\newcommand{\grad}{\textnormal{grad}~}
\newcommand{\curl}{\textnormal{curl}~}
\newcommand{\proj}{{\rm proj}} % projection

%%%%%% Linear Algebra %%%%%%%%%
\newcommand{\minor}{{\rm minor}}
\newcommand{\trace}{{\rm trace}}
\newcommand{\spn}{{\rm Span}}
\newcommand{\ran}{{\rm range}}
\newcommand{\range}{{\rm range}}
\newcommand{\Hom}{{\rm{Hom}}}
\newcommand{\mbyn}[2]{#1\times #2} % m x n 
\newcommand{\tensor}{{\otimes}} % tensor product
\newcommand{\iso}{{\cong}} % isomorph

%%%%%%% Analysis %%%%%%%%%%%%
\newcommand{\C}{\mathbb{C}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbbm{N}}
\newcommand{\Q}{\mathbbm{Q}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Sp}{\mathbb{S}}
\newcommand{\F}{\mathbb{F}} % Field F
\newcommand{\<}{\langle}
\renewcommand{\>}{\rangle}
\renewcommand{\emptyset}{\varnothing}
\newcommand{\Cn}{\C^n}
\newcommand{\Zn}{\Z^n}
\newcommand{\1}[1]{\mathds{1}_{#1}} % characteristic funtion
\newcommand{\abs}[1]{\lvert#1\rvert}% Absolute value notation


%%%%%%% Operator Algebra %%%%%%%%%%%%
\newcommand{\Bh}{\mathcal{B}(\mathcal{H})} % B(H)
\newcommand{\mnc}{\mathbb{M}_n(\mathbb{C})} % M_n(C) matrix algebra
\newcommand{\mn}[1]{\mathbb{M}_{#1}(\mathbb{C})} % M_n(C) matrix algebra for specific n
\newcommand{\RR}{\mathscr{R}} % von Neumann algebra 'R'
\newcommand{\wkly}{\rightharpoonup} % weak convergence arrow symbol
\newcommand{\norm}[1]{\left| \left| #1 \right| \right|}
\newcommand{\opnorm}[1]{\left| \left| #1 \right| \right|_{\text{op}}}
\newcommand{\supnorm}[1]{\left| \left| #1 \right| \right|_{\text{$\infty$}}}
\newcommand{\dsum}[2]{\bigoplus_{#1}^{#2}} % direct sum
\newcommand{\weaker}{\precsim} % weakness symbol between projections
\newcommand{\strictlyweaker}{\prec} % Strict weakness
\newcommand{\mvnequiv}[1]{\stackrel{\mathclap{\normalfont\tiny\mbox{$#1$}}}{\sim}} % Murray-von Neumman equivalence %% It requires \usepackage{mathtools}

%%%
%%% Mathematical operators (things like sin and cos which are used as
%%% functions and have slightly different spacing when typeset than
%%% variables are defined as follows:
%%%

\DeclareMathOperator{\dist}{dist} % The distance function: dist(x, K)

% Celling and Floor function
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Operations
\newcommand{\ds}{\displaystyle}
\newcommand{\quotes}[1]{\textquotedblleft #1\textquotedblright}


%Define two types of differential symbols in an integral.
\newcommand{\diff}{\mathop{}\!d} %Normal article style
\newcommand{\dd}{\mathop{}\!\mathrm{d}} %Journal style
\newcommand{\pd}[2]{\frac{\partial #1 }{\partial #2}}      % first order partial derivative
\newcommand{\p}{\partial}
\newcommand{\pdS}[2]{\frac{\partial^2 #1 }{\partial #2^2}} % second order partial derivative
\newcommand{\pdT}[2]{\frac{\partial^2 #1 }{\partial #2^2}} % third order partial derivative

% Greeck Letters
\newcommand{\ep}{\varepsilon}


%Fraktur, Caligraphy and mathscr capital letters
\newcommand{\fA}{\mathfrak A}     \newcommand{\sA}{\mathcal A}		\newcommand{\kA}{\mathscr{A}}
\newcommand{\fB}{\mathfrak B}     \newcommand{\sB}{\mathcal B}		\newcommand{\kB}{\mathscr{B}}
\newcommand{\fC}{\mathfrak C}     \newcommand{\sC}{\mathcal C}		\newcommand{\kC}{\mathscr{C}}
\newcommand{\fD}{\mathfrak D}     \newcommand{\sD}{\mathcal D}		\newcommand{\kD}{\mathscr{D}}
\newcommand{\fE}{\mathfrak E}     \newcommand{\sE}{\mathcal E}		\newcommand{\kE}{\mathscr{E}}
\newcommand{\fF}{\mathfrak F}     \newcommand{\sF}{\mathcal F}		\newcommand{\kF}{\mathscr{F}}
\newcommand{\fG}{\mathfrak G}     \newcommand{\sG}{\mathcal G}		\newcommand{\kG}{\mathscr{G}}
\newcommand{\fH}{\mathfrak H}     \newcommand{\sH}{\mathcal H}		\newcommand{\kH}{\mathscr{H}}
\newcommand{\fI}{\mathfrak I}     \newcommand{\sI}{\mathcal I}		\newcommand{\kI}{\mathscr{I}}
\newcommand{\fK}{\mathfrak K}     \newcommand{\sK}{\mathcal K}		\newcommand{\kK}{\mathscr{K}}
\newcommand{\fJ}{\mathfrak J}     \newcommand{\sJ}{\mathcal J}		\newcommand{\kJ}{\mathscr{J}}
\newcommand{\fL}{\mathfrak L}     \newcommand{\sL}{\mathcal L}		\newcommand{\kL}{\mathscr{L}}
\newcommand{\fM}{\mathfrak M}     \newcommand{\sM}{\mathcal M}		\newcommand{\kM}{\mathscr{M}}
\newcommand{\fN}{\mathfrak N}     \newcommand{\sN}{\mathcal N}		\newcommand{\kN}{\mathscr{N}}
\newcommand{\fO}{\mathfrak O}     \newcommand{\sO}{\mathcal O}		\newcommand{\kO}{\mathscr{O}}
\newcommand{\fP}{\mathfrak P}     \newcommand{\sP}{\mathcal P}		\newcommand{\kP}{\mathscr{P}}
\newcommand{\fQ}{\mathfrak Q}     \newcommand{\sQ}{\mathcal Q}		\newcommand{\kQ}{\mathscr{Q}}
\newcommand{\fR}{\mathfrak R}     \newcommand{\sR}{\mathcal R}		\newcommand{\kR}{\mathscr{R}}
\newcommand{\fS}{\mathfrak S}     \newcommand{\sS}{\mathcal S}		\newcommand{\kS}{\mathscr{S}}
\newcommand{\fT}{\mathfrak T}     \newcommand{\sT}{\mathcal T}		\newcommand{\kT}{\mathscr{T}}
\newcommand{\fU}{\mathfrak U}     \newcommand{\sU}{\mathcal U}		\newcommand{\kU}{\mathscr{U}}
\newcommand{\fV}{\mathfrak V}     \newcommand{\sV}{\mathcal V}		\newcommand{\kW}{\mathscr{W}}
\newcommand{\fW}{\mathfrak W}     \newcommand{\sW}{\mathcal W}		\newcommand{\kV}{\mathscr{V}}
\newcommand{\fX}{\mathfrak X}     \newcommand{\sX}{\mathcal X}		\newcommand{\kX}{\mathscr{X}}
\newcommand{\fY}{\mathfrak Y}     \newcommand{\sY}{\mathcal Y}		\newcommand{\kY}{\mathscr{Y}}
\newcommand{\fZ}{\mathfrak Z}     \newcommand{\sZ}{\mathcal Z}		\newcommand{\kZ}{\mathscr{Z}}


%bold vector macros
\newcommand{\bu}{{\bf u}}
\newcommand{\bv}{{\bf v}}
\newcommand{\bw}{{\bf w}}
\newcommand{\bx}{{\bf x}}
\newcommand{\by}{{\bf y}}
\newcommand{\bz}{{\bf z}}
\newcommand{\bX}{{\bf X}}
\newcommand{\bY}{{\bf Y}}
\newcommand{\bZ}{{\bf Z}}
\newcommand{\btheta}{{\bf \theta}}
\newcommand{\bTheta}{{\bf \Theta}}
\newcommand{\bze}{{\bf 0}}
\newcommand{\bT}{{\bf T}}
\newcommand{\bB}{{\bf B}}
\newcommand{\bE}{{\bf E}}
\newcommand{\bN}{{\bf N}}

\hypersetup{
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
}

"""



def main():
    file = Preamble()
    print(file)


if __name__ == '__main__':
    main()