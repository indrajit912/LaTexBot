# LaTeX Bot
#
# Author: Indrajit Ghosh
# Created On: Aug 22, 2023
#

from latex_bot import *
from pathlib import Path


def main():
    root = Path.cwd()
    bot = LaTexBot(root_dir=root)
    bot.show_options()


if __name__ == '__main__':
    main()