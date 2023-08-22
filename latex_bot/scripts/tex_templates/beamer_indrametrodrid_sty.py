INDRAMETRODRID = r"""

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Metropolis + Madrid Beamer Theme
%%% Author : Indrajit Ghosh
%%% Institute : Indian Statistical Institute Bangalore
%%% Email : rs_math1902@isibang.ac.in
%%% Date : May 28, 20222
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



\definecolor{metropolisThemeColor}{rgb}{0.105, 0.214, 0.234}
\definecolor{metropolisBarColor}{rgb}{0.984, 0.0.515, 0.015}

\usetheme{Madrid}

\usefonttheme{professionalfonts}
\usecolortheme[named=metropolisThemeColor]{structure}

\useinnertheme{circles}

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
		
		\hspace{13pt} \large \textcolor{metropolisThemeColor}{{\secname}}
		%\vspace{3pt}
		\begin{center}
			\progressbar@progressbar%
		\end{center}
		
		
		% Or you can uncomment the following to get the whole tbc 
		%\tableofcontents[currentsection]
		
	\end{frame}
}

"""