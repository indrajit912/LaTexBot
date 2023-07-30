# Tests will be performed here.
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023

from latex import *

def main():

    plainart = PlainArticle()
    plainart._tex_template = TexFontTemplates.libris_adf_fourier

    plainart.show_output()
    


if __name__ == '__main__':
    main()
    