# A bot to generate blank LaTeX files
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
# Modified On: Jul 30, 2023
#
# Status: Ongoing
#

from latex import *
from scripts.functions import *

COMPILE_TEX_LIVES_HERE = Path(__file__).resolve().parent / 'compile_tex.py'
CWD = Path.cwd()


def main():
    
    res = choose_from_list(TEX_TEMPLATES.values(), "Choose the template you want:")
    clear_terminal_screen()

    if res == TEX_TEMPLATES['quit']:
        print("Thanks for visiting!")

    elif res == TEX_TEMPLATES['plainart']:
        # TODO: Use latex modules

        # First Read `.yml` file for default config
        # tex_dir = CWD or yml config

        # Create `PlainArticle()` object
        plainart = PlainArticle(
            title="My Plain Aritle",
            authors=[IndraAMS.indrajit],
            body_text="Hello there! I'm using \\LaTeX.",
            project_dir=CWD / "new_plain_art",
            amsartstyle=False
        )
        
        # Create plainart
        plainart.create()

    elif res == TEX_TEMPLATES['newart']:
        # TODO: Article
        newart = Article(
            authors=[IndraAMS.indrajit],
            amsartstyle=False,
            project_dir=CWD / "new_article"
        )
        
        # Create `Article()` object
        newart.create()

    elif res == TEX_TEMPLATES['amsart']:
        # TODO: AMS article
        amsart = AmsArticle(
            authors=[IndraAMS.indrajit],
            packages=IndraAMS.packages,
            theorem_styles=IndraAMS.thmstyles,
            custom_commands=IndraAMS.macros,
            project_dir=CWD / "new_ams_article"
        )

        # Create `AmsArticle()` object
        amsart.create()
        
    else:
        # TODO: Else cases

        article_title = "Your Article's Title Here" # TODO: Take input
        author_name = "Your Name Here"
        email = "someone@somewhere.com"
        address = "Enter your address"

        your_info = {
            "title": article_title,
            "author": author_name,
            "email": email,
            "address": address
        }

        informations = INDRAJIT # Don't forget to update here
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


if __name__ == '__main__':
    main()