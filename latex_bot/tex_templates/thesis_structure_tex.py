THESIS_STRUCTURE = r"""
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{enumitem} % Give extra customization on top of itemize and enumerate

\usepackage{amsmath, amsthm, amssymb} % for various mathematical operations
\usepackage{mathtools}
\usepackage{mathrsfs} % Provides \mathscr command
\usepackage{xfrac} % renders diagonal frac notation: use \sfrac{}{}
\usepackage{dsfont} % renders '1' for characteristic function...

\usepackage{epigraph} % Epigraphs are the pithy quotations often found at the start (or end) of a chapter
\usepackage{lipsum}

\usepackage[
    a4paper,
    bindingoffset=0.2in,
    centering,
    marginparwidth=2in,
    textwidth=5.1in,
    marginparsep=2em,
    top=2.5cm,
    bottom=2.5cm
%    showframe
]{geometry} 

%%
%%%Header styles
%%
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[RE]{\textbf{\textit{\nouppercase{\leftmark}}}}
\fancyhead[LO]{\textbf{\textit{\nouppercase{\rightmark}}}}
\fancyfoot[C]{\thepage} 
\renewcommand{\headrulewidth}{2pt}
\renewcommand{\footrulewidth}{0pt}

%%
%%% Fancy Chapter Styles
%%
\usepackage[Conny]{fncychap}
%Options: Conny, Bjarne, Glenn, Lenny, Sonny, Rejne, Bjornstrup


%%%%
%%%% The next few commands set up the theorem type environments.
%%%% Here they are set up to be numbered section.number, but this can
%%%% be changed.
%%%%

\theoremstyle{plain}% default

\newtheorem{theorem}{Theorem}[chapter]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{prop}{Proposition}[chapter]
\newtheorem{cor}[theorem]{Corollary} % '*' produces an output without numbering

%%
%% If some other type is need, say conjectures, then it is constructed
%% by editing and uncommenting the following.
%%

%\newtheorem{conj}[theorem]{Conjecture} 


%%% 
%%% The following gives definition type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 

\theoremstyle{definition}

\newtheorem{definition}{Definition}[chapter]
\newtheorem{example}{Example}[chapter]
\newtheorem{exercise}[example]{Exercise}

%%
%% Again more of these can be added by uncommenting and editing the
%% following. 
%%

\newtheorem{axiom}[definition]{Axiom}
%\newtheorem{condition}{Condition}
%\newtheorem{hypothesis}[definition]{Hypothesis}
\newtheorem{question}[definition]{Question}


%%% 
%%% The following gives remark type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 

\theoremstyle{remark}

\newtheorem*{remark}{Remark}
\newtheorem*{note}{Note}
\newtheorem{case}{Case}

%% Add more here 
\newtheorem*{notation}{Notation}
%\newtheorem*{summ}{Summary}
%\newtheorem*{acknow}{Acknowledgment}

\renewcommand\qedsymbol{$\blacksquare$} % redefining the qed symbol

%%%
%%% The following, if uncommented, numbers equations within sections.
%%% 
\numberwithin{equation}{section}

%%
%%% Setting Tcolorbox for boxed 'theorems'
%%
\usepackage{xcolor}
\usepackage{tikz-cd} % Online editor: https://tikzcd.yichuanshen.de/
\usepackage[most]{tcolorbox}

% Usages: \begin{tcolorbox} Here is some text! \end{tcolorbox}

\newtcbtheorem{theo}{Theorem}{}{theorem}
%  \begin{theo}{Name} My theorem  statement \end{theo}
 

%%%%%%%%%% Bibliography management %%%%%%%%%%
\usepackage[titletoc]{appendix}

\usepackage[english]{babel}
\usepackage{csquotes}
\usepackage[nottoc]{tocbibind}
\usepackage[
backend=bibtex,
style=alphabetic,
sorting=ynt
]{biblatex}
\addbibresource{bibliography.bib}


%%% Hyper reference set up
\usepackage[bookmarksopen,bookmarksnumbered]{hyperref}
\hypersetup{
	pdftitle={New PhD Thesis},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Mathematics},
	pdfcreationdate={\today},
	pdfcreator={Write a creator name (e.g. MikTeX)},
	pdfkeywords={Write your list of keywords},
	colorlinks=true,
	linkcolor={cyan},
	%    filecolor=magenta,      
	urlcolor=blue,
	citecolor=magenta,
	pdfpagemode=UseOutlines,
}
\usepackage{bookmark}

\usepackage{imakeidx}
\makeindex[program=makeindex,options=-s style.ist,columns=2,intoc=true]


%%%%%%%%%%% Glossaries and Acronyms %%%%%%%%%%%%%
\usepackage[acronym]{glossaries-extra}
\setabbreviationstyle[acronym]{long-short}

% Create your own acronyms
\newacronym{vna}{vNa}{von Neumann algebra} % use as: \gls{vna}
\newacronym{dct}{DCT}{Dominated Convergence Theorem}
\newacronym{masa}{MASA}{Maximal Abelian Self-adjoint Algebra}

\makeglossaries

"""