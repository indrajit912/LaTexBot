# Tests will be performed here.
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023

from latex import *

def main():

    dir_ = Path.home() / "Desktop" / "project_dir"

    plainart = PlainArticle(
        project_dir=dir_,
        tex_template=TexFontTemplates.helvetica_fourier_it
    )

    plainart.create()


if __name__ == '__main__':
    main()
    