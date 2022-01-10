m1 = r"""

%%%%%%%%%%%% References %%%%%%%%%%%%
    
    %  NOTE: To complile the references do the followings:
    %       pdflatex main.tex
    %       bibtex main.aux
    %       pdflatex main.tex
    %       pdflatex main.tex
    %

\documentclass[12pt]{amsart}

\input{structure.tex}
\input{math_constants.tex}


%Main Article
\begin{document}


"""
m2 = "" # variable title text
m3 = "    %For multiple authors just repeat the following pattern\n"
m4 = "" # variable author text
m5 = "" # variable address text
m6 = "" # email

m7 = r"""
    %%\urladdr{https://www.mypage.com} % Delete if not wanted.

    \maketitle

    %%%
    %%% The following is for the abstract.  The abstract is optional and
    %%% if not used just delete, or comment out, the following.
    %%%

    \begin{abstract}
    \lipsum[1]
    \end{abstract}


    %%%%%%%%%%%% Sections %%%%%%%%%%%%

    \section{Title of First Section}
    \lipsum[1-2]

    \section{Title of Second Section}
    \lipsum[2-3]



    %%%%%%%%%%%% References %%%%%%%%%%%%
    
    %  NOTE: To complile the references do the followings:
    %       pdflatex main.tex
    %       bibtex main.aux
    %       pdflatex main.tex
    %       pdflatex main.tex
    %

    \medskip
    \bibliographystyle{plain} % Alvailable styles: plain, alpha, abbrv, ieeetr, unsrt
    \nocite{*}
    \bibliography{references.bib} 

\end{document}
"""

main_tex_constants = (m1, m3, m7)