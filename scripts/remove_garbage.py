# Script to rm `latex_bot/latex/tex_garbage` dir
#
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023
#
# Use it from the root by the following cmd
#   `env/bin/python3 scripts/remove_garbage.py`

from pathlib import Path
import shutil

TEX_GARBAGE_DIR = Path(__file__).parent.resolve().parent / "latex_bot" / "latex" / "tex_garbage"

def remove_tex_garbage():
    # Make sure the directory exists before attempting to delete
    if TEX_GARBAGE_DIR.exists() and TEX_GARBAGE_DIR.is_dir():
        shutil.rmtree(TEX_GARBAGE_DIR)
        print(f"Directory {TEX_GARBAGE_DIR} and its contents have been deleted.")
    else:
        print(f"Directory {TEX_GARBAGE_DIR} does not exist.")

def main():
    remove_tex_garbage()

if __name__ == '__main__':
    main()