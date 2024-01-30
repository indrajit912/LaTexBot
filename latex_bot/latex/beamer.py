# A module for Beamer Template.
#
# Author: Indrajit Ghosh
# Created on: Jan 29, 2024
#

from .latex import *
from .articles import AmsArticle
from .utils import compile_tex

from pathlib import Path
from typing import List

__all__ = ["Beamer"]


class Beamer:
    """
    A class representing Beamer LaTeX document.

    Author: Indrajit Ghosh
    Date: Jan 29, 2024

    Attributes that this class would create:
    - Beamer._main_tex
        TexFile
    - Beamer._preamble
        TexFile
    - Beamer._reference_bib
        TexFile
    - Beamer._sections
        [TexFile, ..., TexFile]
    - Beamer._indra_metrodrid_sty
        TexFile

    Class-level Attributes:
    - Beamer.default_title
        Default title for the presentation.
    - Beamer.default_author
        Default author for the presentation.
    - Beamer.default_date
        Default date for the presentation using LaTeX's \today.
    - Beamer.default_project_dir
        Default project directory using Path.cwd().

    Methods:
    - __init__(self, ...)
        Initializes a Beamer instance with various parameters.
    - __str__(self) -> str
        String representation of the Beamer instance.
    - create(self)
        Creates the Beamer
    - _update(self)
        Updates the Beamer instance by calling internal update methods.
    - _update_preamble(self)
        Updates the preamble based on attributes.
    - _update_reference_bib(self)
        Updates references based on attributes.
    - _update_main_tex(self)
        Updates the main TexFile for the project.
    - _default_beamer_packages()
        Returns a list of default TexPackage instances for Beamer.
    - _default_beamer_custom_cmds()
        Returns a string containing default custom commands for Beamer.
    - _default_beamer_sections()
        Returns a list of default BeamerSection instances.
    - _get_indra_metrodrid_theme()
        Returns LaTeX code for the Beamer theme 'indrametrodrid'.
    """
    default_theme = "IndraMetrodrid"
    default_title = "Presentation Title Here"
    default_author = "Indrajit Ghosh"
    default_date = r"\today"
    default_project_dir = Path.cwd() / "new_beamer"

    def __init__(
        self,
        theme:str=None,
        title:str=None,
        subtitle:str=None,
        author:str=None,
        institute:str=None,
        institute_code:str=None,
        email:str=None,
        purpose:str=None,
        date:str=None,
        packages:List[TexPackage] = None,
        theorem_styles:str = None,
        custom_commands:str = None,
        sections:List[TexFile] = None,
        references:list=None,
        project_dir:Path=None,
        *,
        short_title:str=None,
        pdfsubject:str = "Mathematics Presentation",
        pdfcreator:str = "MixTeX",
        pdfcreationdate:str = r"\today",
    ):
        self._theme:str = (
            theme if theme is not None
            else self.default_theme
        )
        self._title:str = (
            title if title is not None
            else self.default_title
        )

        self._subtitle:str = (
            subtitle if subtitle is not None
            else ''
        )

        self._author:str = (
            author if author is not None
            else self.default_author
        )

        self._institute = (
            institute if institute is not None
            else ''
        )

        self._institute_code = (
            institute_code if institute_code is not None
            else ''
        )

        self._email = (
            Email(email) if email is not None
            else ''
        )

        self._purpose = (
            purpose if purpose is not None
            else ''
        )

        self._date:str = (
            self.default_date if date is None
            else date
        )

        self._packages:list = (
            packages
            if packages is not None
            else self._default_beamer_packages()
        )

        self._theorem_styles:str = (
            theorem_styles
            if theorem_styles is not None
            else Preamble._default_ams_theorem_styles()
        )

        self._custom_commands:str = (
            custom_commands
            if custom_commands is not None
            else self._default_beamer_custom_cmds()
        )

        self._sections:list = (
            sections
            if sections is not None
            else self._default_beamer_sections()
        )

        self._references:list = (
            references
            if references is not None
            else AmsArticle._default_references()
        )

        self._project_dir:Path = (
            self.default_project_dir if project_dir is None
            else Path(project_dir)
        )

        self._short_title:str = (
            short_title
            if short_title is not None
            else ''
        )

        self._pdfsubject = pdfsubject
        self._pdfcreator = pdfcreator
        self._pdfcreationdate = pdfcreationdate

        # Setting up Beamer Project components
        self._sections_dir:Path = self._project_dir / "sections"

        # IndraMetrodrid Theme
        self._indra_metrodrid_sty:TexFile = TexFile(
            classfile=True,
            body_text=self._get_indra_metrodrid_theme(),
            filename="beamerthemeIndraMetrodrid",
            file_extension='.sty',
            author="Indrajit Ghosh"
        )

        self._update()


    def __str__(self) -> str:
        self._update()
        return self._main_tex.__str__()

    def create(self, _compile:bool=True):
        """
        Creates the Beamer
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

        # Writing TexFiles 
        print(f" - Writing `{self._preamble.filename}{self._preamble.file_extension}`...")
        self._preamble.write(
            tex_dir=self._project_dir
        )

        print(f" - Writing `{self._main_tex.filename}{self._main_tex.file_extension}`...")
        self._main_tex.write(
            tex_dir=self._project_dir
        )

        if self._theme == 'IndraMetrodrid':
            print(f" - Writing `{self._indra_metrodrid_sty.filename}{self._indra_metrodrid_sty.file_extension}`...")
            self._indra_metrodrid_sty.write(
                tex_dir=self._project_dir
            )


        if self._references:
            print(f" - Writing `{self._reference_bib.filename}{self._reference_bib.file_extension}`...")
            self._reference_bib.write(
                tex_dir=self._project_dir
            )

        print("\n - Writing sections...")

        for sec in self._sections:
            print(f" -- Writing `{sec.filename}{sec.file_extension}`...")
            sec.write(
                tex_dir = self._sections_dir
            )

        if _compile:
            _main_tex:Path = self._project_dir / (self._main_tex.filename + self._main_tex.file_extension)

            compile_tex(
                texfile=_main_tex,
                tex_compiler='pdflatex',
                output_format='.pdf',
                bibtex=True
            )
        

        print(f"\n\nProject Dir: `{self._project_dir}`\n")


    def _update(self):
        """
        Updates the `beamer`. This method should be called
        whenever an attr is set.

        This method calls the following methods:
            self._update_preamble()
            self._update_reference_bib()
            self._update_main_tex()
        """
        self._update_preamble()
        self._update_reference_bib()
        self._update_main_tex()

    def _update_preamble(self):
        """
        Updates the preamble.
        If at any  moment `self._authors` gets updated this function 
        should be called to update the `self._preamble`.
        """
        self._preamble:Preamble = Preamble(
            filename="preamble",
            packages=self._packages,
            theorem_styles=self._theorem_styles,
            custom_commands=self._custom_commands,
            author=self._author
        )

    def _update_reference_bib(self):
        """
        Updates references
        """
        if self._references:
            _ref_body_text = ""
            for ref in self._references:
                _ref_body_text += ref

            self._reference_bib = TexFile(
                filename="references",
                classfile=True,
                file_extension=".bib",
                body_text=_ref_body_text,
                author=self._author
            )

    def _update_main_tex(self):
        """
        This method will update main `TexFile` for the project
        Updates the `self._main_tex` attr
        """
        _main_pre_cmds = r"\usetheme{" + self._theme + "}%\n"
        _main_pre_cmds += (
            r"\newcommand{\Title}{" + self._title + "}%"
            + "\n"
            + r"\newcommand{\SubTitle}{" + self._subtitle + "}%"
            + "\n"
            + r"\newcommand{\Author}{" + self._author + "}%"
            + "\n"
            + r"\newcommand{\ShortTitle}{" + self._short_title + "}%"
            + "\n"
            + r"\newcommand{\InstituteName}{" + self._institute + "}%"
            + "\n"
        )

        if self._institute_code:
            _main_pre_cmds += r"\newcommand{\InstituteCode}{" + self._institute_code + "}%\n"

        if self._email:
            _main_pre_cmds += r"\newcommand{\Email}{" + self._email + "}%\n"

        if self._purpose:
            _main_pre_cmds += r"\newcommand{\Purpose}{" + self._purpose + "}%\n"

        _main_pre_cmds += r"""
%%--------------------------------------------------------------
%%%	       PDF Constants
%%--------------------------------------------------------------
"""
        _main_pre_cmds += (
            r"\newcommand{\pdfTitle}{" + self._title + "}%"
            + "\n"
            r"\newcommand{\pdfAuthor}{" + self._author + "}%"
            + "\n"
            + r"\newcommand{\pdfSubject}{" + self._pdfsubject + "}%"
            + "\n"
            + r"\newcommand{\pdfCreator}{" + self._pdfcreator + "}%"
            + "\n"
            + r"\newcommand{\pdfCreationDate}{" + self._pdfcreationdate + "}%"
            + "\n"
        )

        _main_pre_cmds += (
            "\n"
            + r"\title[\ShortTitle]{\Title}"
            + "%\n"
            + r"\subtitle{\SubTitle}"
            + "%\n"
            + r"\author{\Author}"
            + "%\n"
            + r"\institute"
        )

        if self._institute_code:
            _main_pre_cmds += r"[\InstituteCode]"

        if self._email:
            _main_pre_cmds += r"{\InstituteName \\ \Email}%"
        else:
            _main_pre_cmds += r"{\InstituteName}%"
        
        _main_pre_cmds += (
            "\n\n"
            + r"\date["
            + self._date
            + r"]{\Purpose}"
            + "%\n"
        )

        _main_preamble = "\n" + r"\input{" + self._preamble.filename + "}\n"

        _main_post_doc_cmds = (
            r"\frame{\titlepage}"
            + "%\n"
            + r"\frame{\tableofcontents}"
            + "%\n"
        )

        _main_body_text = ""

        if self._sections:
            for sec in self._sections:
                _main_body_text += (
                    "\n"
                    + r"\input{" + self._sections_dir.name + "/" + sec._filename
                    + "}%\n\n"
                )

        else:
            _main_body_text += r"\lipsum[1]"

        # Add references
        if self._references:
            _main_body_text += (
                "\n" + "%" + "-"*60 + "%\n%" + " " * 20
                + "References"
                + "\n" + "%" + "-"*60 + "%" + " " * 20
                + "\n"
                + r"\section{References}%"
                + "\n"
            )
            _frame_txt = (
                r"""
    \medskip
    \bibliographystyle{alpha} % Alvailable styles: plain, alpha, abbrv, ieeetr, unsrt
    \nocite{*}
    """
                + r"\bibliography{"
                + self._reference_bib.filename + '.bib'
                + "}%\n"
            )
            _frame_ref = Frame(
                title="References",
                options=['allowframebreaks'],
                text=_frame_txt
            )

            _main_body_text += _frame_ref.__str__()
        
        self._main_tex = TexFile(
            tex_compiler="pdflatex",
            output_format=".pdf",
            documentclass=r"\documentclass{beamer}",
            preamble=_main_preamble,
            pre_doc_commands=_main_pre_cmds,
            post_doc_commands=_main_post_doc_cmds,
            body_text=_main_body_text,
            file_extension=".tex",
            filename="main",
            classfile=False
        )

    @staticmethod
    def _default_beamer_packages():
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
                name="hyperref",
                associated_cmds=[
                    r"""
\hypersetup{
	pdftitle={\pdfTitle},
	pdfauthor={\pdfAuthor},
	pdfsubject={\pdfSubject},
	pdfcreationdate={\pdfCreationDate},
	pdfcreator={\pdfCreator},
	pdfpagemode=UseOutlines
}
"""
                ]
            ),
            TexPackage(
                name="tikz",
                associated_cmds = [r"\usetikzlibrary{calc,matrix,arrows}"]
            ),
            TexPackage(
                name="tikz-cd",
                associated_cmds=[
                    r"""\tikzcdset{ampersand replacement=\&}"""
                ],
                comment="Online editor: https://tikzcd.yichuanshen.de/"
            ),
            TexPackage(
                name="lipsum"
            ),
            TexPackage(
                name="babel",
                options=["english"]
            ),
            TexPackage(
                name="natbib",
                associated_cmds=[r"\setbeamertemplate{theorems}[numbered]"]
            ),
            TexPackage(name="xcolor"),
        ]
    
    @staticmethod
    def _default_beamer_custom_cmds():
        return r"""
% Color constants : usages- \textcolor{<colorName>}{<text>}
\definecolor{indraRed}{rgb}{0.593, 0.183, 0.183}
\definecolor{indraPink}{rgb}{0.858, 0.188, 0.478}
\definecolor{indraBlue}{rgb}{0, 0.199, 0.398}
\definecolor{madridBlue}{rgb}{0.199, 0.199, 0.695}
\definecolor{metropolisThemeColor}{rgb}{0.105, 0.214, 0.234}
\definecolor{metropolisBarColor}{rgb}{0.984, 0.0.515, 0.015}
\definecolor{UBCblue}{rgb}{0.04706, 0.13725, 0.26667} % UBC Blue (primary)
\definecolor{UBCgrey}{rgb}{0.3686, 0.5255, 0.6235} % UBC Grey (secondary)
"""

    def _default_beamer_sections(self):
        """
        Returns a `list` of default `BeamerSection`s which Indrajit 
        uses for `beamer` sections

        Returns:
        --------
            `list[BeamerSection(), ..., BeamerSection()]`
        """
        intro = BeamerSection(
            heading="Introduction",
            filename="introduction",
            author=self._author
        )

        intro.add_frame(
            Frame(
                title="Frame Title Here",
                text = r"""
    Etiam euismod. Fusce facilisis lacinia dui. Suspendisse potenti. In mi erat,
    cursus id, nonummy sed, ullamcorper eget, sapien. Praesent pretium,
    magna in eleifend egestas, pede pede pretium lorem!
    
    \begin{thm}[von Neumann]
    	
    	Let $A$ be a self-adjoint operator acting on the Hilbert space $\mathcal{H}$. Then there exists a unique projection valued measure (POVM) $\mu:\mathcal{B}_{\mathbb{R}}\to \mathcal{B}(\mathcal{H})$ such that
    	
    	\[
    		A = \int_{\mathbb{R}} \lambda \ \mathrm{d}\mu(\lambda)
    	\]
    	
    \end{thm}
    
	\pause

	\begin{ex}
		Phasellus eu tellus sit amet tortor gravida placerat.
		Integer sapien est, iaculis in, pretium quis,
	\end{ex}
"""
            )
        )
    
        intro.add_frame(
            Frame(
                title="Another Frame Title",
                text=r"""
    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit,
    vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida
        
       
    \begin{rem}
    	If $A$ is bounded self-adjoint operator on $\mathcal{H}$ and $\psi\in \mathcal{H}$ be a unit vector then there exist a unique probability measure $\mu$ on $\mathbb{R}$ such that for all $m$
    	
    	\[
    		\langle A^m\psi, \psi \rangle = \int_{\mathbb{R}} \lambda^m \ \mathrm{d}\mu(\lambda)
    	\]
    \end{rem}
"""
            )
        )

        sect = BeamerSection(
            heading="Another Section Here",
            filename="section",
            author=self._author
        )
        sect.add_frame(
            Frame(
                title="New Frame",
                text=r"\lipsum[1]"
            )
        )

        return [intro, sect]
    
    @staticmethod
    def _get_indra_metrodrid_theme():
        """
        This function returns the LaTeX code required for the 
        Beamer theme `indrametrodrid` which is basically a 
        combination of Metropolis and Madrid!
        """
        return r"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Metropolis + Madrid Beamer Theme
%%% Author : Indrajit Ghosh
%%% Institute : Indian Statistical Institute Bangalore
%%% Email : rs_math1902@isibang.ac.in
%%% Date : May 28, 2022
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\definecolor{metropolisThemeColor}{rgb}{0.105, 0.214, 0.234}
\definecolor{metropolisBarColor}{rgb}{0.984, 0.0.515, 0.015}

\usetheme{Madrid}

\usefonttheme{professionalfonts}
\usecolortheme[named=metropolisThemeColor]{structure}

\useinnertheme{circles}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%% Progressbar %%%%%%%%%%%%%
%%%%%%%% Author: Indrajit Ghosh
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\makeatletter
\def\progressbar@progressbar{} % the progress bar
\newcount\progressbar@tmpcounta% auxiliary counter
\newcount\progressbar@tmpcountb% auxiliary counter
\newdimen\progressbar@pbht %progressbar height
\newdimen\progressbar@pbwd %progressbar width
\newdimen\progressbar@tmpdim % auxiliary dimension

\progressbar@pbwd=\linewidth
\progressbar@pbht=1.5pt

% the progress bar
\def\progressbar@progressbar{%
	
	\progressbar@tmpcounta=\insertframenumber
	\progressbar@tmpcountb=\inserttotalframenumber
	\progressbar@tmpdim=\progressbar@pbwd
	\multiply\progressbar@tmpdim by \progressbar@tmpcounta
	\divide\progressbar@tmpdim by \progressbar@tmpcountb
	
	\begin{tikzpicture}[very thin]
		\draw[indraBlue!30,line width=\progressbar@pbht]
		(0pt, 0pt) -- ++ (\progressbar@pbwd,0pt);
		\draw[draw=none]  (\progressbar@pbwd,0pt) -- ++ (2pt,0pt);
		
		\draw[metropolisBarColor,line width=\progressbar@pbht]
		(0pt, 0pt) -- ++ (\progressbar@tmpdim,0pt);
		
	\end{tikzpicture}%
}


\AtBeginSection[]
{
	\begin{frame}
		\frametitle{}
		
		\hspace{13pt} \large \textcolor{metropolisThemeColor}{{\secname}}
		%\vspace{3pt}
		\begin{center}
			\progressbar@progressbar%
		\end{center}
		
		
		% Or you can uncomment the following to get the whole tbc 
		%\tableofcontents[currentsection]
		
	\end{frame}
}
"""