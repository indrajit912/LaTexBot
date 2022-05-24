MAIN = r"""
% Author: Indrajit Ghosh
% Thesis LaTeX 

%  Commands for genrating pdf
%       1. pdflatex <main.tex>
%       2. bibtex <main.aux>
%       3. pdflatex <main.tex>
%

\documentclass[a4paper,11pt,twoside,openany]{book}

\input{thesis_structure.tex}
\input{math_constants.tex}

\begin{document}

    \input{Chapters/titlepage.tex}
    \thispagestyle{empty}
    \clearpage
    
    \frontmatter
    
    \chapter*{Abstract}
    \input{Chapters/abstract.tex}
    \addcontentsline{toc}{chapter}{Abstract}
    \clearpage
    \thispagestyle{empty}
    
    \chapter*{Dedication}
    \input{Chapters/dedication.tex}
    \addcontentsline{toc}{chapter}{Dedication}
    \clearpage
    \thispagestyle{empty}
    
    \chapter*{Declaration}
    \input{Chapters/declaration.tex}
    \addcontentsline{toc}{chapter}{Declaration}
    \clearpage
    \thispagestyle{empty}
    
    \chapter*{Acknowledgements}
    \input{Chapters/acknowledgements.tex}
    \addcontentsline{toc}{chapter}{Acknowledgements}
    \clearpage
    \thispagestyle{empty}
    
    \cleardoublepage
    \pdfbookmark[section]{\contentsname}{toc}
    \tableofcontents
    \clearpage
    \thispagestyle{empty}
    \cleardoublepage
    
    \mainmatter
    
    \chapter{Introduction}
    \input{Chapters/introduction.tex}
    
    \chapter{Type Chapter Name}
    \input{Chapters/chapter01.tex}
    
    \chapter{Name Here}
    \input{Chapters/chapter02.tex}
    
    \chapter{Write a Chapter Name}
    \input{Chapters/chapter03.tex}
    
    \chapter{Conclusion}
    \input{Chapters/conclusion.tex}
    
    \backmatter
    
    \appendix
    \chapter{Appendix Title}
    \input{Chapters/appendix.tex}
    
    \nocite{*}
    \printbibliography[
    heading=bibintoc,
    title={Bibliography}] 
    
    \printglossary[type=\acronymtype]
    
    \printindex

\end{document}

"""
