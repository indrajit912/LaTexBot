# A library containing all packages, theorem styles
# and custom commands that I usually use in `article`
#
# Author: Indrajit Ghosh
# Date: Aug 23, 2023
#

from .latex import *

class IndraArt:
    r"""
    Packages I usually use for `article`
    Author: Indrajit Ghosh
    Date: Aug 23, 2023
    
    LaTeX packages, thm style and macros that I usually use in `article` doc.

    Attributes:
    -----------
        `packages`: Packages that I usually use in `amsart` document.
                e.g.-   \usepackage[utf8]{inputenc}

        `thmstyles` : Theorem Styles I use in `amsart`
                e.g.-   \theoremstyle{plain}
                        \newtheorem{theorem}{Theorem}[section]
                        \newtheorem{prop}[theorem]{Proposition}
                        \newtheorem{lem}[theorem]{Lemma}

        `macros`: Macros I use in `amsart`
                e.g.-   \newcommand{\C}{\mathbb{C}}
                        \newcommand{\R}{\mathbb{R}}
                        \newcommand{\N}{\mathbb{N}}
    """

    packages:list = [
        TexPackage(name="inputenc", options=['utf8']),
        TexPackage(name="fontenc", options=['T1']),
        TexPackage(
            name="lmodern",
            comment="To get high quality fonts"
        ),
        TexPackage(
            name="geometry",
            options=[
                "top=1in",
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
            name="lastpage",
            comment="To get the last page of the article"
        ),
        TexPackage(
            name="bbm",
            comment="For typing `set of natural nums`, e.g - \mathbbm{N}"
        ),
        TexPackage(name="mathtools"),
        TexPackage(name="mathrsfs", comment="renders \mathscr cmd"),
        TexPackage(name="xfrac", comment="renders diagonal frac notation: use \\sfrac{}{}"),  
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
        TexPackage(name="array"),
        TexPackage(
            name="enumitem",
            comment="Give extra customization on top of itemize and enumerate"
        ),
        TexPackage(
            name="tikz-cd",
            comment="Online editor: https://tikzcd.yichuanshen.de/"
        ),
        TexPackage(
            name="microtype",
            comment="To disable `ligatures` by using `\\DisableLigatures`.",
            associated_cmds=[r"\DisableLigatures{encoding = *, family = *}"],
        ),
        TexPackage(name="graphicx"),
        TexPackage(name="xcolor"),
        TexPackage(name="lipsum"),
        TexPackage(
            name="dsfont",
            comment="Renders '1' for characteristic function..."
        ),
        TexPackage(
            name="babel",
            options=["english"]
        ),
        TexPackage(
            name="titling",
            comment="Customizing the title section",
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
                r"\renewcommand\Affilfont{\fontsize{10}{10.8}\selectfont}",
                r"\renewcommand*{\Authsep}{, }",
                r"\renewcommand*{\Authand}{{\bfseries\ and }}",
                r"\renewcommand*{\Authands}{{\bfseries\ , and }}",
                r"\setlength{\affilsep}{1em}",
                r"\newsavebox\affbox"
            ]
        ),
        TexPackage(
            name="abstract",
            comment="Allows abstract customization",
            associated_cmds=[
                r"\renewcommand{\abstractnamefont}{\normalfont\bfseries} % Set the 'Abstract' text to bold",
                r"\renewcommand{\abstracttextfont}{\normalfont\small\itshape} % Set the abstract itself to small italic text",
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
            name="csquotes",
            comment="Required to generate language-dependent quotes in the bibliography"
        ),
        TexPackage(
            name="tocbibind",
            comment="To add bibliogrphy to the table of content"
        ),
        TexPackage(
            name="biblatex",
            options=[
                "style=alphabetic",
                "sorting=ynt",
                "backend=biber"
            ],
            associated_cmds=[r"\addbibresource{\bibFile} % The filename of the bibliography"]
        )
    ]