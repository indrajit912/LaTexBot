# Script to rm latex/garbage_dir
#
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023
#

from pathlib import Path

GARBAGE_DIR = Path(__file__).parent.resolve().parent / "latex_bot" / "latex" / "tex_garbage"


def main():
    print(GARBAGE_DIR)
    GARBAGE_DIR.rmdir()


if __name__ == '__main__':
    main()