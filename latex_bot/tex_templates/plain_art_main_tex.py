m1 = r"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%	Title and Author(s) informations
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

# Title
# Author
# Dept
# Institute

m2 = r"""\date{\today} % keep \date{} for no date 

%%%%% PDF informations %%%%%%%%%%%%%%%%%%%%%%
\newcommand{\PDFsubject}{Your Subject}
\newcommand{\PDFkeywords}{Keyword1, Keyword2, etc}
\newcommand{\PDFcreator}{e.g. MikTeX or Overleaf}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


\documentclass[12pt, twoside]{article}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
\usepackage{graphicx}
\usepackage{xcolor} %For coloring texts and objects
\usepackage{lipsum}
\usepackage{authblk} %For Author Titling and affiliating Purpose
%%%%%%%%%%%%%%%% PDF Setups %%%%%%%%%%%
\usepackage{hyperref}
\hypersetup{
	pdftitle={\Title},
	pdfauthor={\Author},
	pdfsubject={\PDFsubject},
	pdfcreationdate={\today},
	pdfcreator={\PDFcreator},
	pdfkeywords={\PDFkeywords},
	colorlinks=true,
	linkcolor={cyan},
	%    filecolor=magenta,      
	urlcolor=blue,
	citecolor=magenta,
	pdfpagemode=UseOutlines,
}


\title{\Title} % Title of the Document
\author{\textsc{\Author}} % Author name
\affil{\normalsize \Department} % Author's Department
\affil{\normalsize \Institute} % Authors Institute

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%% Title customizations %%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\usepackage{titling} % Customizing the title section
\setlength{\droptitle}{-4\baselineskip} % Move the title up
\pretitle{\begin{center}\LARGE\bfseries} % Article title formatting
	\posttitle{\end{center}} % Article title closing formatting
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



%Main Article
\begin{document}

\maketitle
\thispagestyle{empty}

\lipsum % Write your article here


\end{document}

"""

plain_art_main_constants = (m1, m2)