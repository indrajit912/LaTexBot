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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%  Custom Beamer Styles 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


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
		
		\hspace{13pt} \large \textcolor{UBCblue}{{\secname}}
		%\vspace{3pt}
		\begin{center}
			\progressbar@progressbar%
		\end{center}
		
		
		% Or you can uncomment the following to get the whole tbc 
		%\tableofcontents[currentsection]
		
	\end{frame}
}



%%
%% This is the end of the preamble.
%% 


"""