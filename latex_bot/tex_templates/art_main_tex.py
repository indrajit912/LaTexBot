m1 = r"""


\documentclass[12pt, twoside]{article}

\usepackage{authblk} %For Author Titling and affiliating Purpose

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%	Title and Author(s) informations
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

# \title{Article Title Here} % Title of the Document

m3 = r"""
\newcommand\shorttitle{Give a short title here} % Write your short title
"""

# \author{\textsc{Indrajit Ghosh}} % Give first author name here

m5 = r""" % For multiple authors do: \author[1]{Author1 Name}
%\author[2]{\textsc{Second Author name}} % Second author name here
\newcommand\authors{Author1 Name} % Write the Authors name separated by comma here 
"""

# \newcommand{\firstauthoremail}{rs\_math1902@isibang.ac.in} % First author email

m7 = r"""
%\newcommand{\secondauthoremail}{soumyashant@gmail.com} % Second author email

"""

# \affil{\normalsize Statistics-Mathematics Unit} % Department
# \affil{\normalsize Indian Statistical Institute Bangalore} % Institute

m10 = r"""

{
	\makeatletter
	\renewcommand\AB@affilsepx{: \protect\Affilfont}
	\makeatother
	
	%	\affil[ ]{Email ids}
	
	\makeatletter
	\renewcommand\AB@affilsepx{, \protect\Affilfont}
	\makeatother
	
	\affil{\firstauthoremail} % For multiple authors do: \affil[1]{\firstauthoremail}
%	\affil[2]{\secondauthoremail} % Second author email
}


\date{\today} % keep \date{} for no date 


\usepackage{indratexpreamble}


%Main Article
\begin{document}

\maketitle
\thispagestyle{empty}


\begin{abstract}
\noindent \lipsum[1]
\end{abstract}

\section{Section 1 Title}
\input{sections/section1}

\section{Section 2 Title}
\input{sections/section2}

%References.
\newpage
\nocite{*}
\printbibliography[
heading=bibintoc,
title={References}] 

\end{document}
"""

art_main_tex_constants = (m1, m3, m5, m7, m10)