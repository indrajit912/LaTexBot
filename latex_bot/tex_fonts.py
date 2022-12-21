# Script to handle LaTeX fonts
#
# Author: Indrajit Ghosh
# Created On: Dec 21, 2022
#

from pathlib import Path
from datetime import datetime
import os
from uuid import uuid4

LATEX_FONTS = {
    'default': {'family': 'cmr', 'name': 'Computer Modern'},
    'code': {'family': '\\ttfamily', 'name': 'TeX Default Typewriter'},
    'courier': {'family': 'pcr', 'name': 'Courier'},
    'artemisia': {'family': 'artemisia', 'name': 'Artemisia'},
    'charter': {'family': 'bch', 'name': 'Charter'},
    'bodoni': {'family': 'bodoni', 'name': 'Bodoni'},
    'concrete': {'family': 'ccr', 'name': 'Computer Concrete'},
    'complutum': {'family': 'complutum', 'name': 'Complutum'},
    'inconsolata': {'family': 'fi4', 'name': 'Inconsolata'},
    'verasans': {'family': 'fvs', 'name': 'Bitstream Vera Sans'},
    'baskerville': {'family': 'gfsbaskerville', 'name': 'Baskerville'},
    'lx': {'family': 'llcmss', 'name': 'LX'},
    'latinmodern': {'family': 'lmr', 'name': 'Latin Modern'},
    'latinmodernsans': {'family': 'lmss', 'name': 'Latin Modern Sans'},
    'latintypewriter': {'family': 'lmtt', 'name': 'Latin Modern Typewriter'},
    'kerkis': {'family': 'mak', 'name': 'Kerkis'},
    'garamond': {'family': 'ugm', 'name': 'Garamond'},
    'neohellenic': {'family': 'neohellenic', 'name': 'Neohellenic'},
    'avantgarde': {'family': 'pag', 'name': 'Avant Garde'},
    'bookman': {'family': 'pbk', 'name': 'Bookman'},
    'helvetica': {'family': 'phv', 'name': 'Helvetica'},
    'schoolbook': {'family': 'pnc', 'name': 'New Century Schoolbook'},
    'porson': {'family': 'porson', 'name': 'Porson'},
    'palatino': {'family': 'ppl', 'name': 'Palatino'},
    'times': {'family': 'ptm', 'name': 'Times'},
    'utopia': {'family': 'put', 'name': 'Utopia'},
    'chancery': {'family': 'pzc', 'name': 'Zapf Chancery'},
    'adventor': {'family': 'qag', 'name': 'TeX Gyre Adventor'},
    'bonum': {'family': 'qbk', 'name': 'TeX Gyre Bonum'},
    'cursor': {'family': 'qcr', 'name': 'TeX Gyre Cursor'},
    'schola': {'family': 'qcs', 'name': 'TeX Gyre Schola'},
    'heros': {'family': 'qhv', 'name': 'TeX Gyre Heros'},
    'pagella': {'family': 'qpl', 'name': 'TeX Gyre Pagella'},
    'termes': {'family': 'qtm', 'name': 'TeX Gyre Termes'},
    'chorus': {'family': 'qzc', 'name': 'TeX Gyre Chorus'},
    'solomos': {'family': 'solomos', 'name': 'Solomos'},
    'greektimes': {'family': 'txr', 'name': 'Greek Times'},
    'didot': {'family': 'udidot', 'name': 'Didot'},
    'uncial': {'family': 'uncl', 'name': 'Uncial'},
    'linuxbio': {
        'family': 'LinuxBiolinumT-OsF',
        'name': 'Linux Biolinum'
    },
    'linuxliber': {
        'family': 'LinuxLibertineT-OsF',
        'name': 'Linux Libertine'
    },
}


def get_system_fonts():
    """
    Returns a lilst of all fonts installed in the system
    """
    system_fonts = []
    filename = uuid4().hex + '.txt'
    cmd = f"fc-list : family | sort | uniq > {filename}"
    os.system(cmd)
    
    with open(filename, 'r') as f:
        for e in f.readlines():
            system_fonts.append(e.strip())
    
    os.unlink(filename)
    return system_fonts


def get_font_env(env_name:str="my_font", fontfamily:str=None):
    """
    This will returns a LaTeX environment with `env_name` for the font
    with `fontfamily`.

    This env can be used within the TeX doc by:
        \begin{env_name}
            Here is a text with this font!
        \end{env_name}

    Returns:
    --------
        `str`: "\newenvironment{<env_name>}{\fontfamily{<fontfamily>}\selectfont}{\par}"
        
    """
    return (
        "\\newenvironment{" + 
        env_name + 
        "}{\\fontfamily{" +
        fontfamily + 
        "}\\selectfont}{\\par}"
    )

def generate_fonts_tex_file(where_to_save:Path=Path.cwd()):
    """
    This will create `fonts.tex` file which will contain all envs for
    various fonts which can be used in a TeX doc.
        
        `fonts.tex`:
        '''
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            % Environments for various fonts in LaTeX
            % Author: Indrajit Ghosh
            % Created On: {now}

            % Usage:
            %    1. First add this file in your preamble by `\input`
            %    2. use \\begin <env_name> 
            %                     ... 
            %            \end <env_name>
            %
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            % Font name: Computer Modern; Env name: default_font
            \newenvironment{default_font}{\fontfamily{cmr}\selectfont}{\par}


            % Font name: Bodoni; Env name: bodoni
            \newenvironment{bodoni}{\fontfamily{bodoni}\selectfont}{\par}

            % Font name: Computer Concrete; Env name: concrete
            \newenvironment{concrete}{\fontfamily{ccr}\selectfont}{\par}

                                so on
        '''
    """
    fonts_tex_file = Path(where_to_save) / 'fonts.tex'
    with open(fonts_tex_file, "w") as f:
        now = datetime.now().strftime("%b %d, %Y")
        msg = f"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Environments for various fonts in LaTeX
% Author: Indrajit Ghosh
% Created On: {now}
"""   
        msg += r"""

% Usage:
%    1. First add this file in your preamble by `\input{fonts}`
%    2. Use any of the following font family as shown below
%            \begin{verasans_font}
%                 Here is some text written in `verasans_font`
%            \end{verasans_font}

% NOTE: The following command will change the whole document's font
% to the font with FONT_FAMILY.
%    \renewcommand{\rmdefault}{<FONT_FAMILY>}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

"""

        f.write(msg)
        f.write('\n')
        for font_code, font in LATEX_FONTS.items():
            env_name = font_code + '_font'
            tex_env = get_font_env(env_name=env_name, fontfamily=font['family'])
            f.write('% Font name: ' + font['name'] + f"; Env name: {env_name}" + '\n')
            f.write(tex_env)
            f.write("\n\n")


def generate_sample_tex_file(filepath:Path=Path.cwd() / "fonts_demo.tex"):
    """
    This will create a `.tex` file to showcase all fonts available in the
    dictionary LATEX_FONTS.
    """
    now = datetime.now().strftime("%b %d, %Y")
    preamble = f"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Various LaTeX fonts
% Author: Indrajit Ghosh
% Created On: {now}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
    preamble += r"""
\documentclass[12pt, twoside]{article}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}

\title{Fonts in \LaTeX}
\author{Indrajit Ghosh}
\date{\today}

%Main Article
\begin{document}
\maketitle
"""
    maindoc = ''
    for font_env_name, font in LATEX_FONTS.items():
        font_env_name += '_font'
        env_str = get_font_env(env_name=font_env_name, fontfamily=font['family'])
        sample_text = (
            r"\begin{" + 
            font_env_name + 
            r"}" + 
            "\n" + 
            f"This text is written in the font: `{font['name']}'" + 
            "\n" + 
            r"\end{" + 
            font_env_name + 
            r"}" + 
            "\n\n"
        )
        maindoc += (
            "\n" + 
            env_str +
            '\n' + 
            sample_text
        )

    end_doc = r"\end{document}"

    tex_file_content = preamble + maindoc + end_doc
    with open(filepath, 'w') as f:
        f.write(tex_file_content)


def main():
    garbage_dir = './garbage/'
    # generate_fonts_tex_file(garbage_dir)
    generate_sample_tex_file(garbage_dir + 'spam.tex')
    pass


if __name__ == '__main__':
    main()