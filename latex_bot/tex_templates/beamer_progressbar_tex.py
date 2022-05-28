PROGRESSBAR = r"""

\definecolor{pbblue}{HTML}{0A75A8}% color for the progress bar and the circle

\makeatletter
\def\progressbar@progressbar{} % the progress bar
\newcount\progressbar@tmpcounta% auxiliary counter
\newcount\progressbar@tmpcountb% auxiliary counter
\newdimen\progressbar@pbht %progressbar height
\newdimen\progressbar@pbwd %progressbar width
\newdimen\progressbar@rcircle % radius for the circle
\newdimen\progressbar@tmpdim % auxiliary dimension

\progressbar@pbwd=\linewidth
\progressbar@pbht=1pt
\progressbar@rcircle=2.5pt

% the progress bar
\def\progressbar@progressbar{%
	
	\progressbar@tmpcounta=\insertframenumber
	\progressbar@tmpcountb=\inserttotalframenumber
	\progressbar@tmpdim=\progressbar@pbwd
	\multiply\progressbar@tmpdim by \progressbar@tmpcounta
	\divide\progressbar@tmpdim by \progressbar@tmpcountb
	
	\begin{tikzpicture}
		\draw[pbblue!30,line width=\progressbar@pbht]
		(0pt, 0pt) -- ++ (\progressbar@pbwd,0pt);
		
		\filldraw[pbblue!30] %
		(\the\dimexpr\progressbar@tmpdim-\progressbar@rcircle\relax, .5\progressbar@pbht) circle (\progressbar@rcircle);
		
		\node[draw=pbblue!30,text width=3.5em,align=center,inner sep=1pt,
		text=pbblue!70,anchor=east] at (0,0) {\insertframenumber/\inserttotalframenumber};
	\end{tikzpicture}%
}

\addtobeamertemplate{headline}{}
{%
	\begin{beamercolorbox}[wd=\paperwidth,ht=4ex,center,dp=1ex]{white}%
		\progressbar@progressbar%
	\end{beamercolorbox}%
}
\makeatother

"""