s1 = r"""
%Some packages I commonly use.
\usepackage{hyperref}
\hypersetup{
"""

s4 = r"""
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

\usepackage{graphicx}

\usepackage{xcolor} %For coloring texts and objects
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

\usepackage{framed}
\usepackage[normalem]{ulem}
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{mathtools}
\usepackage{enumitem} % Give extra customization on top of itemize and enumerate
\usepackage[utf8]{inputenc}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
\usepackage{tikz-cd} % Online editor: https://tikzcd.yichuanshen.de/
\usepackage{lipsum}
\usepackage{authblk} %For Author Titling and affiliating Purpose


%Basic Structure
\newcommand{\attn}[1]{\textbf{#1}}
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}{Lemma}[section]
\newtheorem{cor}{Corollary}[section]
\newtheorem{prop}{Proposition}[section]

\theoremstyle{definition}
\newtheorem*{definition}{Definition}
\newtheorem*{example}{Example}
\newtheorem*{note}{Note}
\newtheorem{exercise}{Exercise}
\newtheorem{remark}{Remark}[section]
\newcommand{\bproof}{\bigskip {\bf Proof. }}
\newcommand{\eproof}{\hfill\qedsymbol}
\newcommand{\Disp}{\displaystyle}
\newcommand{\qe}{\hfill\(\bigtriangledown\)}
\setlength{\columnseprule}{1 pt}
\renewcommand\qedsymbol{$\blacksquare$}


%----------------------------------------------------------------------------------------
%	Bibliography
%----------------------------------------------------------------------------------------

\usepackage[english]{babel}% English language hyphenation

\usepackage[autostyle=true]{csquotes} % Required to generate language-dependent quotes in the bibliography
\usepackage[nottoc]{tocbibind} %To add bibliogrphy to the table of content

\usepackage[
backend=bibtex,
style=alphabetic,
sorting=ynt
]{biblatex} % Use the bibtex backend with the authoryear citation style (which resembles APA)
"""

structure_tex_constants = (s1, s4)