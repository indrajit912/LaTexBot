# A bot to generate LaTeX files
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
# Modified On: Jul 30, 2023
#
# Status: Ongoing
#

from .latex import *
from .scripts.functions import *
import subprocess
import os

COMPILE_TEX_LIVES_HERE = Path(__file__).resolve().parent / 'compile_tex.py'
CWD = Path.cwd()

class LaTexBot:
    """
    A Bot that can create LaTeX templates!

    Author: Indrajit Ghosh
    """
    
    def __init__(self, root_dir:Path=CWD):
        self._root_dir = root_dir

    def show_options(self):
        res = choose_from_list(TEX_TEMPLATES.values(), "Choose the template you want:")
        clear_terminal_screen()

        if res == TEX_TEMPLATES['quit']:
            print("Thanks for visiting!")
        elif res == TEX_TEMPLATES['plainart']:
            self.create_plain_article()
        elif res == TEX_TEMPLATES['newart']:
            self.create_new_article()
        elif res == TEX_TEMPLATES['amsart']:
            self.create_ams_article()
        elif res == TEX_TEMPLATES['beamer']:
            self.create_beamer()
        else:
            self.create_custom_article(res)

    def create_plain_article(self):
        # PlainArticle
        plainart = PlainArticle(
            title="My Plain Aritle",
            authors=[IndraAMS.indrajit],
            body_text="Hello there! I'm using \\LaTeX.",
            project_dir=self._root_dir / "new_plain_art",
            amsartstyle=False
        )
        plainart.create()

    def create_new_article(self):
        # Article
        newart = Article(
            authors=[IndraAMS.indrajit],
            amsartstyle=False,
            packages=IndraArt.packages,
            theorem_styles=IndraAMS.thmstyles,
            custom_commands=IndraAMS.macros,
            project_dir=self._root_dir / "new_article"
        )
        newart.create()

    def create_ams_article(self):
        # AMS article
        amsart = AmsArticle(
            authors=[IndraAMS.indrajit],
            packages=IndraAMS.packages,
            theorem_styles=IndraAMS.thmstyles,
            custom_commands=IndraAMS.macros,
            project_dir=self._root_dir / "new_ams_article"
        )
        amsart.create()

    def create_beamer(self):
        # Beamer
        beamer = Beamer(
            title="Sample Presentation Title Here",
            subtitle="Here is subtitle",
            author="Indrajit Ghosh",
            institute="Indian Statistical Institute Bangalore",
            email="rs_math1902@isibang.ac.in",
            institute_code="ISI",
            purpose="Write the Conference Name -- Mmm YYYY",
            project_dir=self._root_dir / "new_beamer"
        )
        beamer.create()

    def create_custom_article(self, res):
        # TODO: Else cases
        article_title = "Your Article's Title Here"  # TODO: Take input
        author_name = "Your Name Here"
        email = "someone@somewhere.com"
        address = "Enter your address"

        your_info = {
            "title": article_title,
            "author": author_name,
            "email": email,
            "address": address
        }

        informations = INDRAJIT  # Don't forget to update here
        informations.setdefault("title", article_title)

        output_dir_path = setup_output_directory(res)

        # Creating tex, bib, ist etc files
        write_indrapreamble_sty(tex_template=res, output_dir=output_dir_path)
        create_main_tex(tex_template=res, info=informations, output_dir=output_dir_path)

        # Compiling the `main.tex` file
        os.chdir(output_dir_path)
        subprocess.run(["python3", str(COMPILE_TEX_LIVES_HERE)])

        clear_terminal_screen()

        print(f"\n\n\t\t::: YOUR TeX WORKING DIRECTORY :::\n\n   {output_dir_path}\n\n")


def main():
    print("LaTexBot module!")


if __name__ == '__main__':
    main()