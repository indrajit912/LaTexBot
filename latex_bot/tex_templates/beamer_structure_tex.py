BEAMER_STRUCTURE = r"""
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathrsfs} % renders \mathscr cmd
\usepackage{dsfont} % renders '1' for characteristic function...
\usepackage{array}
\usepackage{xfrac} % renders diagonal frac notation: use \sfrac{}{}
\usepackage{verbatim}
\usepackage{graphicx}
%\usepackage{graphics}
%\usepackage{color}
\usepackage{hyperref}
\hypersetup{
	pdftitle={Decomposing Matrices},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Operator Algebras},
	pdfcreationdate={\texorpdfstring{\today}{\today}},
	pdfcreator={MikTeX},
	pdfkeywords={Matrix Decomposition, Operator Algebras, von-Neumann Algebras}
}

\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{tikz-cd} % Online editor: https://tikzcd.yichuanshen.de/
\tikzcdset{ampersand replacement=\&} % only needs for 'beamer'
\usepackage{lipsum}
\usetikzlibrary{matrix,arrows}
\usepackage[english]{babel}
\usepackage{natbib} % for bibliography purposes


\setbeamertemplate{theorems}[numbered]


\theoremstyle{plain}% default
\newtheorem{thm}{Theorem}[section]
\newtheorem{lem}[thm]{Lemma}
\newtheorem{prop}[thm]{Proposition}
\newtheorem*{cor}{Corollary} % '*' produces an output without numbering


\theoremstyle{definition}
\newtheorem*{defn}{Definition}
\newtheorem{question}{Question}


\theoremstyle{example}
\newtheorem*{xmpl}{Example}


\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\newtheorem*{newnote}{Note}

%%
%% This is the end of the preamble.
%% 


"""