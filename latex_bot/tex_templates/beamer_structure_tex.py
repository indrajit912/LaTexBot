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
	pdftitle={Presentation Title Here},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Mathematics},
	pdfcreationdate={\texorpdfstring{\today}{}},
	pdfcreator={MikTeX},
	pdfkeywords={Keyword1, Keyword2}
}
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

\newtheorem{defn}{Definition}[section]
\newtheorem{xmpl}{Example}[section]
\newtheorem{question}{Question}


\theoremstyle{remark}

\newtheorem*{remark}{Remark}
\newtheorem*{newnote}{Note}

%%
%% This is the end of the preamble.
%% 


"""