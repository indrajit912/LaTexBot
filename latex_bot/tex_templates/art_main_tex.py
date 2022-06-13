m1 = r"""

\documentclass[12pt, twoside]{article}

\usepackage{indratexpreamble}

"""

m6 = r"""
	%\and  %Uncomment if 2 authors are required, duplicate these 4 lines if more
	%\textsc{Soumyashant Nayak}\thanks{Corresponding author} \\ % Second author's name
	%\normalsize Stat-Math Unit, \\ 
	%\normalsize Indian Statistical Institute \\ % Second author's institution
	%\normalsize \href{mailto:someone@somewhere.com}{someone@somewhere.com} % Second author's email address
}
\date{\today} % Use \date{} to omit a date




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

art_main_tex_constants = (m1, m6)