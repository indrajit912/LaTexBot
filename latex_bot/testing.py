# Tests will be performed here.
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023

from latex import *

def main():

    msg = r"""
Hi, I am Indrajit...

Here is some Math equation:
\[
    \int f\ d\mu = 0
\]
"""
    plainart = PlainArticle(body_text=msg)
    plainart._tex_template = TexFontTemplates.slitex

    plainart.show_output()
    

if __name__ == '__main__':
    main()
    