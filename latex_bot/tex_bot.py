# A bot to generate blank LaTeX files
#
# Author: Indrajit Ghosh
#
# Date: May 24, 2022
#
# Status: Ongoing
#


from functions import *

COMPILE_TEX_LIVES_HERE = HOME / "Documents/latex_files/scripts_for_tex/latex_bot/compile_tex.py"


def main():

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
    
    
    res = choose_from_list(TEX_TEMPLATES.values(), "Choose the template you want:")

    output_dir_path = setup_output_directory(res)

    # Creating tex, bib, ist etc files
    create_math_constants_tex(output_dir_path)
    create_structure_tex(tex_template=res, output_dir=output_dir_path)
    create_main_tex(tex_template=res, info=informations, output_dir=output_dir_path)

    # Compiling the `main.tex` file
    os.chdir(output_dir_path)
    subprocess.run(["python3", str(COMPILE_TEX_LIVES_HERE)])

    os.system('clear')

    print(f"\n\n\t\t::: YOUR TeX WORKING DIRECTORY :::\n\n   {output_dir_path}\n\n")


if __name__ == '__main__':
    main()