# A library containing all packages, theorem styles
# and custom commands that I usually use in `amsart`
#
# Author: Indrajit Ghosh
# Date: Jul 21, 2023
#

from latex import TexPackage

# TODO: Add all your AMS packages here
class IndraAMS:
    """
    Packages I usually use for `amsart`
    Author: Indrajit Ghosh
    Date: Jul 21, 2023
    """

    """
    LaTeX packages that I usually use in `amsart` doc.
    """
    packages = [
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


    thmstyles = r"""

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

    macros = r"""
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
