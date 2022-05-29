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

\usetheme{IndraMetrodrid} % Custom theme : Metropolis + Madrid

\usepackage{indratexpreamble}


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
        \frametitle{Frame Title Here}
        
        Etiam euismod. Fusce facilisis lacinia dui. Suspendisse potenti. In mi erat,
        cursus id, nonummy sed, ullamcorper eget, sapien. Praesent pretium,
        magna in eleifend egestas, pede pede pretium lorem!
        
        \begin{definition}[Indrajit, 2022]
        	
        	Nam dui ligula, fringilla a, euismod sodales, sollicitudin vel, wisi. Morbi
        	auctor lorem non justo. Nam lacus libero, pretium at, lobortis vitae,
        	ultricies et, tellus. Donec aliquet, tortor sed
        	
        \end{definition}
    
    	\pause
    
    	\begin{xmpl}
    		Phasellus eu tellus sit amet tortor gravida placerat.
    		Integer sapien est, iaculis in, pretium quis,
    	\end{xmpl}
        
    }

    \frame
    {
        \frametitle{Frame Title here}
        
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit,
        vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida
        mauris. Nam arcu libero, nonummy eget, consectetuer id, vulputate a,
        magna. Donec vehicula augue eu neque. Pellentesque habitant morbi
        tristique senectus et netus et malesuada fames ac turpis egestas. Mauris
        ut leo. Cras viverra metus rhoncus sem. Nulla et lectus vestibulum urna
        fringilla ultrices. Phasellus eu tellus sit amet tortor.
        
       
        \begin{newnote}
        	Donec cursus id, nonummy sed, ullamcorper eget, sapien. Praesent pretium, magna in eleifend egestas, pede pede pretium lorem!
        \end{newnote}
        
        
    }


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \section{Section Title Here}

    \frame
    {
        \frametitle{Frame Title Here}
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit,
        vestibulum ut, placera. Curabitur dictum gravida
        
        \begin{enumerate}
        	\item Hodifjlk dkjfsl shfwieo sdkfls.
        	\item Sofdkd dlsj id jbsk, dsjifj.
        	\item Yoin dsjfkh djfkhk wifhsdkfj jsjdflk kjhdskf!
        	\item Lorem iplsu Jkldif.
        \end{enumerate}
    }


	\section{Section Title Here}
	
	\section{Section Title Here}
	
	\section{Section Title Here}

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