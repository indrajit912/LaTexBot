# A module for LaTeX
#
# Author: Indrajit Ghosh
#
# Date: Jun 17, 2023
#

from datetime import datetime
import copy, re, tempfile
from pathlib import Path

__all__ = ["TexFile", "TexPackage"]

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`


class TexPackage:
    """
    A class to represent a `LaTeX` Package

    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    """
    def __init__(self, name:str, options:list=None):
        self._name = name
        self._options = (
            ",".join(options) 
            if options is not None
            else ""
        )


    def __str__(self):
        if self._options == '':
            return r"\usepackage{" + self._name + r"}" + "%\n"
        else:
            return r"\usepackage[" + self._options + r"]{" + self._name + r"}" + "%\n"
    
    def __add__(self, right):
        return self.__str__() + right.__str__()
    
    def __radd__(self, left):
        if isinstance(left, str):
            return left.__add__("\n" + self.__str__())
        


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
    file_extension : :class:`str`
        File extension, e.g. `.tex`, `.bib`, `.sty` etc
    filename : :class: `str`
        Name of the TeX file, e.g. `main`, `bibliography` etc
    author : :class: `str`
        Author of the TexFile
    classfile : :class: `bool`
        If this is true then the TexFile will be assumed to be a class file like `sty`, `cls` etc.
        In `True` case the above attributes will be '' and `body_text` can be updated.
    """

    default_documentclass = r"\documentclass[12pt, twoside]{article}"
    default_preamble = r"""
\usepackage[english]{babel}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
"""
    default_body_text = "\nYourTextHere\n"
    default_tex_compiler = "pdflatex"
    default_output_format = ".pdf"
    default_pre_doc_commands = "\\date{\\today} % keep \\date{} for no date\n" + \
                                            "\\newcommand{\\Author}{Indrajit Ghosh}\n"
                                            
    default_post_doc_commands = ""
    default_file_extension = ".tex"
    default_filename = "untitled"
    default_author = "Indrajit Ghosh"


    def __init__(
            self,
            tex_compiler:str=None,
            output_format:str=None,
            documentclass:str=None,
            preamble:str=None,
            body_text:str=None,
            pre_doc_commands:str=None,
            post_doc_commands:str=None,
            file_extension:str=None,
            filename:str=None,
            author:str=None,
            classfile:bool=False,
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

        self._file_extension = (
            file_extension
            if file_extension is not None
            else TexFile.default_file_extension
        )

        self._filename = (
            filename
            if filename is not None
            else TexFile.default_filename
        )

        self._author = (
            author
            if author is not None
            else TexFile.default_author
        )

        self._classfile = classfile

        if self._classfile:
            self._documentclass = self._preamble = self._post_doc_commands = \
                                                        self._pre_doc_commands = ''

        self._rebuild()

    def _rebuild(self):
        """
        Rebuilds the entire TeX template text from ``\\documentclass`` to 
        ``\\end{document}`` according to all settings and choices.
        """

        self._fileinfo = "\n" + "%"*60 + f"\n%\t{self._filename}{self._file_extension}\n" + \
                                f"%\tAuthor: {self._author}\n" + \
                                f"%\tDate: {TODAY}\n" + "%"*60 + "\n\n"
        
        self.body = self._fileinfo
        
        if not self._classfile:
            self.body += (
                "\n"
                + self._documentclass
                + "%\n%\n"
                + self._pre_doc_commands
                +"%\n"
                + self._preamble
                + "%\n%\n"
                + r"\begin{document}"
                + "%\n"
            )

        self.body += self._body_text

        if not self._classfile:
            self.body += (
                "%\n"
                + self._post_doc_commands
                + "%\n"
                + r"\end{document}"
                + "%\n"
            )

        self.body += (
            "\n"
            + "%" * 60 + "\n"
            + f"%\t\tEnd of `{self._filename}{self._file_extension}`\n"
            + "%" * 60 + "\n"
        )


    def __str__(self):
        return self.body
    
    def __repr__(self):
        classname = self.__class__.__name__
        return f"{classname}({self._documentclass})"
    
    @property
    def metadata(self):
        return {
            "tex_compiler": self._tex_compiler,
            "output_format": self._output_format,
            "documentclass": self._documentclass,
            "preamble": self._preamble,
            "body_text": self._body_text,
            "pre_doc_commands": self._pre_doc_commands,
            "post_doc_commands": self._post_doc_commands,
            "file_extension": self._file_extension,
            "filename": self._filename,
            "author": self._author
        }
    
    @metadata.setter
    def metadata(self, newdata:dict):
        if 'tex_compiler' in newdata.keys():
            self._tex_compiler = newdata['tex_compiler']
        
        if 'output_format' in newdata.keys():
            self._output_format = newdata['output_format']

        if 'documentclass' in newdata.keys():
            self._documentclass = newdata['documentclass']
        
        if 'preamble' in newdata.keys():
            self._preamble = newdata['preamble']
        
        if 'body_text' in newdata.keys():
            self._body_text = newdata['body_text']
        
        if 'pre_doc_commands' in newdata.keys():
            self._pre_doc_commands = newdata['pre_doc_commands']
        
        if 'post_doc_commands' in newdata.keys():
            self._post_doc_commands = newdata['post_doc_commands']
        
        if 'file_extension' in newdata.keys():
            self._file_extension = newdata['file_extension']

        if 'filename' in newdata.keys():
            self._filename = newdata['filename']
        
        if 'author' in newdata.keys():
            self._author = newdata['author']

        self._rebuild()
    
    def add_to_preamble(self, txt, prepend=False):
        """
        Adds stuff to the TeX template's preamble (e.g. definitions, packages). 
        Text can be inserted at the beginning or at the end of the preamble.

        Parameters
        ----------
        txt : :class:`string`
            String containing the text to be added, e.g. ``\\usepackage{hyperref}``
        prepend : Optional[:class:`bool`], optional
            Whether the text should be added at the beginning of the preamble, i.e. 
            right after ``\\documentclass``. Default is to add it at the end of the 
            preamble, i.e. right before ``\\begin{document}``
        """
        if prepend:
            self._preamble = "\n" + txt + "\n" + self._preamble
        else:
            self._preamble += "\n" + txt + "\n"
        self._rebuild()

    
    def add_to_document(self, txt):
        """Adds txt to the TeX template just after \\begin{document}, e.g. ``\\boldmath``

        Parameters
        ----------
        txt : :class:`str`
            String containing the text to be added.
        """
        self._post_doc_commands += "\n" + txt + "\n"
        self._rebuild()


    @property
    def tex_complier(self):
        return self._tex_compiler
    
    @tex_complier.setter
    def tex_compiler(self, compiler:str):
        self._tex_compiler = compiler
        self._rebuild()

    @property
    def output_format(self):
        return self._output_format

    @output_format.setter
    def output_format(self, new_format:str):
        self._output_format = new_format
        self._output_format()

    @property
    def documentclass(self):
        return self._documentclass

    @documentclass.setter
    def documentclass(self, newclass:str):
        self._documentclass = newclass
        self._rebuild()

    @property
    def preamble(self):
        return self._preamble
    
    @preamble.setter
    def preamble(self, newpreamble:str):
        self._preamble = newpreamble
        self._rebuild()

    @property
    def body_text(self):
        return self._body_text
    
    @body_text.setter
    def body_text(self, newtext:str):
        self._body_text = newtext
        self._rebuild()

    @property
    def pre_doc_commands(self):
        return self._pre_doc_commands

    @pre_doc_commands.setter
    def pre_doc_commands(self, newcmds:str):
        self._pre_doc_commands = newcmds
        self._rebuild()

    @property
    def post_doc_commands(self):
        return self._post_doc_commands
    
    @post_doc_commands.setter
    def post_doc_commands(self, newcmds:str):
        self._post_doc_commands = newcmds
        self._rebuild()

    @property
    def file_extension(self):
        return self._file_extension
    
    @file_extension.setter
    def file_extension(self, newext:str):
        if not newext.startswith('.'):
            newext = "." + newext
        self._file_extension = newext
        self._rebuild()

    @property
    def filename(self):
        return self._filename
    
    @filename.setter
    def filename(self, newname:str):
        # If the `newname` ends with an extension then strip it
        self._filename = newname.split('.')[0]
        self._rebuild()

    @property
    def classfile(self):
        return self._classfile
    
    @classfile.setter
    def classfile(self, new:bool):
        self._classfile = new
        self._rebuild()


    def copy(self):
        return copy.deepcopy(self)
    
    def write(self, tex_dir:Path):
        """
        Writes the TexFile() into the given directory `tex_dir`
        and returns the TeX file path

        Parameter:
        ----------
        `tex_dir`: `Path`
                  The directory where to create the TeX file
        Returns:
        --------
        TeX file path: `Path`
        """
        texfilepath = Path(tex_dir) / (self.filename + self.file_extension)
        with open(texfilepath, 'w') as f:
            f.write(self.body)

        return texfilepath
    
    @staticmethod
    def latex_escape(text:str):
        """
        This function accepts plain text and return the TeX escaped text.

        Parameter:
        ----------
            `text`: `str`, a plain text message; This msg should not be any 
                            standard LaTeX command such as `\begin{document}`.
        
        Returns:
        --------
            `str`; the message escaped to paste it into a `.tex` file
        """
        tex_conversion = {
            '&': r'\&',
            '%': r'\%',
            '$': r'\$',
            '#': r'\#',
            '_': r'\_',
            '{': r'\{',
            '}': r'\}',
            '~': r'\textasciitilde{}',
            '^': r'\^{}',
            '\\': r'\textbackslash{}',
            '<': r'\textless{}',
            '>': r'\textgreater{}',
        }

        regex = re.compile(
            '|'.join(
                re.escape(str(key)) for key in sorted(
                    tex_conversion.keys(), key=lambda item : -len(item)
                )
            )
        )

        return regex.sub(
            lambda match: tex_conversion[match.group()], text
        )
    
    def _compile(self, tex_dir:Path):
        """
        TODO: This function tries to compile the TexFile inside the `_tmp_path`
        """
        # Create `_tmp_path`
        # _tmp_path = tempfile.mkdtemp(prefix="latexbot-tmp.")

        # Write the TexFile inside the _tmp_path
        # self.write(tex_dir=_tmp_path)

        # print(_tmp_path)


def main():
    file = TexFile()
    file.filename = "main"


if __name__ == '__main__':
    main()