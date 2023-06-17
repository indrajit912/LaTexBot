# A module for LaTeX
#
# Author: Indrajit Ghosh
#
# Date: Jun 17, 2023
#

from datetime import datetime

__all__ = ["TexFile"]

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`


class TexFile:
    """
    TeX templates used to create `plainarticle`, `article`, `amsarticle` etc

    Parameters
    ----------
    tex_compiler : :class:`str`
        The TeX compiler to be used, e.g. ``latex``, ``pdflatex`` or ``lualatex``
    output_format : :class:`str`
        The output format resulting from compilation, e.g. ``.dvi`` or ``.pdf``
    documentclass : :class:`str`
        The command defining the documentclass, e.g. ``\\documentclass[preview]{standalone}``
    preamble : :class:`str`
        The document's preamble, i.e. the part between ``\\documentclass`` and ``\\begin{document}``
    body_text : :class:`str`
        Text in between ``\\begin{document}`` and ``\\end{document}``
    pre_doc_commands : :class:`str`
        Text to be inserted at the very begining of the file, e.g. ``\\newcommand{\Author}{Indrajit Ghosh}``
    post_doc_commands : :class:`str`
        Text (definitions, commands) to be inserted at right after ``\\begin{document}``, e.g. ``\\boldmath``
    """

    default_documentclass = r"\documentclass[12pt, twoside]{article}"
    default_preamble = r"""
\usepackage[english]{babel}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
"""
    default_body_text = "\nYourTextHere\n"
    default_tex_compiler = "pdflatex"
    default_output_format = ".pdf"
    default_pre_doc_commands = f"\n% Author: Indrajit Ghosh\n% Date: {TODAY}\n"
    default_post_doc_commands = ""


    def __init__(
            self,
            tex_compiler:str=None,
            output_format:str=None,
            documentclass:str=None,
            preamble:str=None,
            body_text:str=None,
            pre_doc_commands:str=None,
            post_doc_commands:str=None,
            **kwargs,
    ):
        self._tex_compiler = (
            tex_compiler
            if tex_compiler is not None
            else TexFile.default_tex_compiler
        )

        self._output_format = (
            output_format
            if output_format is not None
            else TexFile.default_output_format
        )

        self._documentclass = (
            documentclass
            if documentclass is not None
            else TexFile.default_documentclass
        )

        self._preamble = (
            preamble
            if preamble is not None
            else TexFile.default_preamble
        )

        self._body_text = (
            body_text
            if body_text is not None
            else TexFile.default_body_text
        )

        self._pre_doc_commands = (
            pre_doc_commands
            if pre_doc_commands is not None
            else TexFile.default_pre_doc_commands
        )

        self._post_doc_commands = (
            post_doc_commands
            if post_doc_commands is not None
            else TexFile.default_post_doc_commands
        )

        self._rebuild()

    def _rebuild(self):
        """
        Rebuilds the entire TeX template text from ``\\documentclass`` to 
        ``\\end{document}`` according to all settings and choices.
        """
        self.body = (
            self._pre_doc_commands
            + "\n"
            + self._documentclass
            + "\n"
            + self._preamble
            + "\n"
            + r"\begin{document}"
            + "\n"
            + self._body_text
            + "\n"
            + r"\end{document}"
            + "\n"
        )

    def __str__(self):
        return self.body
    
    def __repr__(self):
        classname = self.__class__.__name__
        return f"{classname}({self._documentclass})"


    @property
    def tex_complier(self):
        return self._tex_compiler
    
    @tex_complier.setter
    def tex_compiler(self, compiler:str):
        self._tex_compiler = compiler

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, new_format:str):
        self._output_format = new_format

    @property
    def documentclass(self):
        return self._documentclass

    @documentclass.setter
    def documentclass(self, newclass:str):
        self._documentclass = newclass

    @property
    def preamble(self):
        return self._preamble
    
    @preamble.setter
    def preamble(self, newpreamble:str):
        self._preamble = newpreamble

    @property
    def body_text(self):
        return self._body_text
    
    @body_text.setter
    def body_text(self, newtext:str):
        self._body_text = newtext

    @property
    def pre_doc_commands(self):
        return self._pre_doc_commands

    @pre_doc_commands.setter
    def pre_doc_commands(self, newcmds:str):
        self._pre_doc_commands = newcmds

    @property
    def post_doc_commands(self):
        return self._post_doc_commands
    
    @post_doc_commands.setter
    def post_doc_commands(self, newcmds:str):
        self._post_doc_commands = newcmds



def main():
    
    texfile = TexFile()


if __name__ == '__main__':
    main()