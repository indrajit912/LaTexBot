AMS_STRUCTURE = r"""
\usepackage[top=0.9in, bottom=1in, left=1in, right=1in]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{mathtools}
\usepackage{mathrsfs} % renders \mathscr cmd
\usepackage{xfrac} % renders diagonal frac notation: use \sfrac{}{}
\usepackage{dsfont} % renders '1' for characteristic function...
\usepackage{array}
\usepackage{verbatim}
\usepackage{graphicx}
%\usepackage{graphics}
%\usepackage{color}
\usepackage{enumitem} % Give extra customization on top of itemize and enumerate
\usepackage{hyperref}
\hypersetup{
	pdftitle={New AMS Article},
	pdfauthor={Indrajit Ghosh},
	pdfsubject={Mathematics},
	pdfcreationdate={\today},
	pdfcreator={Write a creator name (e.g. MikTeX)},
	pdfkeywords={Write your list of keywords},
	colorlinks=true,
	linkcolor={cyan},
	%    filecolor=magenta,      
	urlcolor=blue,
	citecolor=magenta,
	pdfpagemode=UseOutlines,
}
\usepackage{tikz-cd} % Online editor: https://tikzcd.yichuanshen.de/
\usepackage{lipsum}
\usetikzlibrary{matrix,arrows}
\usepackage[english]{babel}
\usepackage{natbib} % for bibliography purposes

%Header and footer package
%\usepackage{fancyhdr}
%\pagestyle{fancy}


%Sets line spacing to 1 and a half
\linespread{1.1}


%%%%
%%%% The next few commands set up the theorem type environments.
%%%% Here they are set up to be numbered section.number, but this can
%%%% be changed.
%%%%

\theoremstyle{plain}% default

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{prop}[theorem]{Proposition}
\newtheorem*{cor}{Corollary} % '*' produces an output without numbering

%%
%% If some other type is need, say conjectures, then it is constructed
%% by editing and uncommenting the following.
%%

%\newtheorem{conj}[theorem]{Conjecture} 


%%% 
%%% The following gives definition type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 

\theoremstyle{definition}

\newtheorem{definition}{Definition}[section]
\newtheorem{example}{Example}[section]
\newtheorem{exercise}[example]{Exercise}

%%
%% Again more of these can be added by uncommenting and editing the
%% following. 
%%

\newtheorem{axiom}[definition]{Axiom}
%\newtheorem{condition}{Condition}
%\newtheorem{hypothesis}[definition]{Hypothesis}
\newtheorem{question}[definition]{Question}


%%% 
%%% The following gives remark type environments (which only differ
%%% from theorem type environments in the choices of fonts).  The
%%% numbering is still tied to the theorem counter.
%%% 

\theoremstyle{remark}

\newtheorem*{remark}{Remark}
\newtheorem*{note}{Note}
\newtheorem{case}{Case}

%% Add more here 
\newtheorem*{notation}{Notation}
%\newtheorem*{summ}{Summary}
%\newtheorem*{acknow}{Acknowledgment}


%%%
%%% The following, if uncommented, numbers equations within sections.
%%% 

\numberwithin{equation}{section}


%%
%%% My custom theorem styles
%%

\newtheoremstyle{ser}% name
{8pt}% Space above
{8pt}% Space below
{\it}% Body font
{}% Indent amount
{\sf}% Theorem head font
{:}% Punctuation after theorem head
{6mm}% Space after theorem head
{}% Theorem head spec (can be left empty, meaning `normal')

\theoremstyle{ser}
\newtheorem{claim}{Claim}


\newtheoremstyle{serr}% name
{8pt}% Space above
{8pt}% Space below
{\normalfont}% Body font
{}% Indent amount
{\sf}% Theorem head font
{.}% Punctuation after theorem head
{6mm}% Space after theorem head
{}% Theorem head spec (can be left empty, meaning `normal')

\theoremstyle{serr}
\newtheorem{pf_of_claim}{Proof of Claim}

\theoremstyle{ser}
\newtheorem{conj}{Conjecture}

\theoremstyle{ser}
\newtheorem{qn}{Question}


%%
%%% My Custom Environments
%%
%\newenvironment{nam}[args]{begdef}{enddef}
\newenvironment{solution}{\begin{proof}[Solution]}{\end{proof}}


% Here is a different 'checkmark' if you need it uncomment the following cmd
%\def\checkmark{\tikz\fill[scale=0.4](0,.35) -- (.25,0) -- (1,.7) -- (.25,.15) -- cycle;}


%%
%% This is the end of the preamble.
%% 

"""