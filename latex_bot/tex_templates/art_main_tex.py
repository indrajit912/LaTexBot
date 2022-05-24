m1 = r"""
\documentclass[12pt]{article}

\input{structure}
\input{math_constants.tex}


%Main Article
\begin{document}

"""
m2 = "" # variable text
m3 = "" # variable text
m4 = r"""\date{\today\\\small}"""
m5 = "" # variable text

m6 = r"""
\maketitle

\begin{abstract}
\lipsum[1]
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

art_main_tex_constants = (m1, m4, m6)