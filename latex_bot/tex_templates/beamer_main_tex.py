BEAMER_MAIN = r"""
%%%%
% Author: Indrajit Ghosh
% Stat-Math Unit,
% Indian Statistical Institute, Bangalore
%%%%


%  NOTE: To complile the references do the followings:
%       pdflatex main.tex
%       bibtex main.aux
%       pdflatex main.tex
%       pdflatex main.tex
%

\documentclass{beamer}

\usetheme{Madrid}
\usecolortheme{default}


\input{structure}
\input{math_constants}

\title{Presentation Title}
\subtitle{}


\author{Indrajit Ghosh}

\institute[ISI] {Indian Statistical Institute Bangalore\\rs\_math1902@isibang.ac.in}


\date[\today]
{Purpose of the Presentation -- Month 2022}


\begin{document}
	
	\frame{\titlepage} % # 1
	\section[Outline]{}
	\frame{\tableofcontents} % # 2


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	\section{Introduction}

    \frame
    {
        \frametitle{Frame 1 Title here}
        \lipsum[1]
        \pause
        \lipsum[1]
    }

    \frame
    {
        \frametitle{Frame  2 Title here}
        \lipsum[1-2]
    }


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \section{Section 2 Title}

    \frame
    {
        \frametitle{Frame 1 Title here}
        \lipsum[1]
    }


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	%%%%%%%%%%%%%%% References %%%%%%
	\section{References}
	\frame[allowframebreaks] % #
	{ 
		
		\frametitle{References}
		\medskip
		\bibliographystyle{alpha} % Alvailable styles: plain, alpha, abbrv, ieeetr, unsrt
		\nocite{*}
		\bibliography{references.bib} 
	}

	
\end{document}


"""