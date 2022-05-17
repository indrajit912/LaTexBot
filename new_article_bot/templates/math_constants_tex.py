MATH_CONSTANTS = r"""
% Math symbols/terminology I frequently use.
% Author: Indrajit Ghosh



% ########## Without math mode ##########

\newcommand{\matlab}{{\sc Matlab} } % Matlab symbol
\newcommand{\HI}{H$\ddot{\text{o}}$lder's inequality } % Holder Inequality



% ######### Inside Math mode ##########

%%%%%% Calculus Symbols %%%%%%%%%%%%
\newcommand{\cvec}[1]{{\mathbf #1}} % bold R^n vector
\newcommand{\rvec}[1]{\vec{\mathbf #1}} % vector with arrow
\newcommand{\ihat}{\hat{\textbf{\i}}}
\newcommand{\jhat}{\hat{\textbf{\j}}}
\newcommand{\khat}{\hat{\textbf{k}}}
\newcommand{\mdiv}{{\rm div}} % divergence
\newcommand{\grad}{\textnormal{grad}~}
\newcommand{\curl}{\textnormal{curl}~}
\newcommand{\proj}{{\rm proj}} % projection

%%%%%% Linear Algebra %%%%%%%%%
\newcommand{\minor}{{\rm minor}}
\newcommand{\trace}{{\rm trace}}
\newcommand{\spn}{{\rm Span}}
\newcommand{\rem}{{\rm rem}}
\newcommand{\ran}{{\rm range}}
\newcommand{\range}{{\rm range}}
\newcommand{\Hom}{{\rm{Hom}}}
\newcommand{\mbyn}[2]{#1\times #2} % m x n 

%%%%%%% Analysis %%%%%%%%%%%%
\newcommand{\C}{\mathbb{C}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Sp}{\mathbb{S}}
\newcommand{\F}{\mathbb{F}} % Field F
\newcommand{\<}{\langle}
\renewcommand{\>}{\rangle}
\renewcommand{\emptyset}{\varnothing}
\newcommand{\Cn}{\C^n}
\newcommand{\Zn}{\Z^n}
\newcommand{\1}[1]{\mathds{1}_{#1}} % characteristic funtion


%%%%%%% Operator Algebra %%%%%%%%%%%%
\newcommand{\Bh}{\mathcal{B}(\mathcal{H})} % B(H)
\newcommand{\mnc}{\mathbb{M}_n(\mathbb{C})} % M_n(C) matrix algebra
\newcommand{\RR}{\mathscr{R}} % von Neumann algebra 'R'
\newcommand{\wkly}{\rightharpoonup} % weak convergence arrow symbol
\newcommand{\norm}[1]{\left| \left| #1 \right| \right|}
\newcommand{\opnorm}[1]{\left| \left| #1 \right| \right|_{\text{op}}}
\newcommand{\supnorm}[1]{\left| \left| #1 \right| \right|_{\text{$\infty$}}}
\newcommand{\dsum}[2]{\bigoplus_{#1}^{#2}} % direct sum
\newcommand{\weaker}{\precsim} % weakness symbol between projections
\newcommand{\strictlyweaker}{\prec} % Strict weakness
\newcommand{\mvnequiv}[1]{\stackrel{\mathclap{\normalfont\tiny\mbox{$#1$}}}{\sim}} % Murray-von Neumman equivalence %% It requires \usepackage{mathtools}


% Celling and Floor function
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Operations
\newcommand{\ds}{\displaystyle}
\newcommand{\quotes}[1]{\textquotedblleft #1\textquotedblright}


%Define two types of differential symbols in an integral.
\newcommand{\diff}{\mathop{}\!d} %Normal article style
\newcommand{\dd}{\mathop{}\!\mathrm{d}} %Journal style
\newcommand{\pd}[2]{\frac{\partial #1 }{\partial #2}}      % first order partial derivative
\newcommand{\p}{\partial}
\newcommand{\pdS}[2]{\frac{\partial^2 #1 }{\partial #2^2}} % second order partial derivative
\newcommand{\pdT}[2]{\frac{\partial^2 #1 }{\partial #2^2}} % third order partial derivative


%Fraktur, Caligraphy and mathscr capital letters
\newcommand{\fA}{\mathfrak A}     \newcommand{\sA}{\mathcal A}		\newcommand{\kA}{\mathscr{A}}
\newcommand{\fB}{\mathfrak B}     \newcommand{\sB}{\mathcal B}		\newcommand{\kB}{\mathscr{B}}
\newcommand{\fC}{\mathfrak C}     \newcommand{\sC}{\mathcal C}		\newcommand{\kC}{\mathscr{C}}
\newcommand{\fD}{\mathfrak D}     \newcommand{\sD}{\mathcal D}		\newcommand{\kD}{\mathscr{D}}
\newcommand{\fE}{\mathfrak E}     \newcommand{\sE}{\mathcal E}		\newcommand{\kE}{\mathscr{E}}
\newcommand{\fF}{\mathfrak F}     \newcommand{\sF}{\mathcal F}		\newcommand{\kF}{\mathscr{F}}
\newcommand{\fG}{\mathfrak G}     \newcommand{\sG}{\mathcal G}		\newcommand{\kG}{\mathscr{G}}
\newcommand{\fH}{\mathfrak H}     \newcommand{\sH}{\mathcal H}		\newcommand{\kH}{\mathscr{H}}
\newcommand{\fI}{\mathfrak I}     \newcommand{\sI}{\mathcal I}		\newcommand{\kI}{\mathscr{I}}
\newcommand{\fK}{\mathfrak K}     \newcommand{\sK}{\mathcal K}		\newcommand{\kK}{\mathscr{K}}
\newcommand{\fJ}{\mathfrak J}     \newcommand{\sJ}{\mathcal J}		\newcommand{\kJ}{\mathscr{J}}
\newcommand{\fL}{\mathfrak L}     \newcommand{\sL}{\mathcal L}		\newcommand{\kL}{\mathscr{L}}
\newcommand{\fM}{\mathfrak M}     \newcommand{\sM}{\mathcal M}		\newcommand{\kM}{\mathscr{M}}
\newcommand{\fN}{\mathfrak N}     \newcommand{\sN}{\mathcal N}		\newcommand{\kN}{\mathscr{N}}
\newcommand{\fO}{\mathfrak O}     \newcommand{\sO}{\mathcal O}		\newcommand{\kO}{\mathscr{O}}
\newcommand{\fP}{\mathfrak P}     \newcommand{\sP}{\mathcal P}		\newcommand{\kP}{\mathscr{P}}
\newcommand{\fQ}{\mathfrak Q}     \newcommand{\sQ}{\mathcal Q}		\newcommand{\kQ}{\mathscr{Q}}
\newcommand{\fR}{\mathfrak R}     \newcommand{\sR}{\mathcal R}		\newcommand{\kR}{\mathscr{R}}
\newcommand{\fS}{\mathfrak S}     \newcommand{\sS}{\mathcal S}		\newcommand{\kS}{\mathscr{S}}
\newcommand{\fT}{\mathfrak T}     \newcommand{\sT}{\mathcal T}		\newcommand{\kT}{\mathscr{T}}
\newcommand{\fU}{\mathfrak U}     \newcommand{\sU}{\mathcal U}		\newcommand{\kU}{\mathscr{U}}
\newcommand{\fV}{\mathfrak V}     \newcommand{\sV}{\mathcal V}		\newcommand{\kW}{\mathscr{W}}
\newcommand{\fW}{\mathfrak W}     \newcommand{\sW}{\mathcal W}		\newcommand{\kV}{\mathscr{V}}
\newcommand{\fX}{\mathfrak X}     \newcommand{\sX}{\mathcal X}		\newcommand{\kX}{\mathscr{X}}
\newcommand{\fY}{\mathfrak Y}     \newcommand{\sY}{\mathcal Y}		\newcommand{\kY}{\mathscr{Y}}
\newcommand{\fZ}{\mathfrak Z}     \newcommand{\sZ}{\mathcal Z}		\newcommand{\kZ}{\mathscr{Z}}


%bold vector macros
\newcommand{\bu}{{\bf u}}
\newcommand{\bv}{{\bf v}}
\newcommand{\bw}{{\bf w}}
\newcommand{\bx}{{\bf x}}
\newcommand{\by}{{\bf y}}
\newcommand{\bz}{{\bf z}}
\newcommand{\bX}{{\bf X}}
\newcommand{\bY}{{\bf Y}}
\newcommand{\bZ}{{\bf Z}}
\newcommand{\btheta}{{\bf \theta}}
\newcommand{\bTheta}{{\bf \Theta}}
\newcommand{\bze}{{\bf 0}}
\newcommand{\bT}{{\bf T}}
\newcommand{\bB}{{\bf B}}
\newcommand{\bE}{{\bf E}}
\newcommand{\bN}{{\bf N}}

"""