# A module for LaTeX
#
# Author: Indrajit Ghosh
# Created On: Jun 17, 2023
# Modified On: Jul 20, 2023
#

from datetime import datetime
import copy, re, hashlib, subprocess, os, sys
from pathlib import Path
from .utils import open_file, _print_tex_error_from_log

TEX_DIR = Path(__file__).parent / "tex_dir"

__all__ = ["Author", "TexPackage", "TexFile", "TexSection", "Preamble"]

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`

class Author:
    r"""
    A class representing an Article author

    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    """
    _default_name = "Author Name"
    _default_dept = "Dept. of the Author"
    _default_institute = "Institute of the Author"
    _default_addr = [
        "Street No, Name Road",
        "Post Office, City",
        "State - XXX XXX, Country"
    ]

    def __init__(
            self,
            name:str=None,
            department:str=None,
            institute:str=None,
            address:list=None,
            email:str=None,
            current_address:list=None,
            support:str=None
    ):
        self._name = (
            name
            if name is not None
            else self._default_name
        )

        self._dept:str = (
            department
            if department is not None
            else self._default_dept
        )

        self._institute:str = (
            institute
            if institute is not None
            else self._default_institute
        )

        self._addr:list = (
            address
            if address is not None
            else self._default_addr
        )

        _fulladdr = [self._dept, self._institute] + self._addr # `dept\\addr`

        self._amsAddrTeX:str = self._add_comma_to_list(_fulladdr)

        self._email:str = email
        self._curr_addr:list = current_address

        self._currAddrTeX = (
            self._add_comma_to_list(self._curr_addr)
            if self._curr_addr is not None
            else None
        )

        self._support = support

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new:str):
        self._name = new

    @property
    def department(self):
        return self._dept
    
    @department.setter
    def department(self, new:str):
        self._dept = new
    
    @property
    def institute(self):
        return self._institute

    @institute.setter
    def institute(self, new:str):
        self._institute = new

    @property
    def address(self):
        return self._addr
    
    @address.setter
    def address(self, new:list):
        self._addr = new

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new:str):
        self._email = new

    @property
    def current_address(self):
        return self._curr_addr
    
    @current_address.setter
    def current_address(self, new:list):
        self._curr_addr = new

    @property
    def support(self):
        return self._support
    
    @support.setter
    def support(self, new:str):
        self._support = new


    @staticmethod
    def _add_texlinebreak_to_list(lst:list):
        """
        This function accepts a list and add `\\` i.e. r"\textbackslash{}\textbackslash{}"
        in between each elements.

        Parameter(s):
        -------------
            `lst`: `list`

        Returns:
        --------
            `str`

        Example:
        --------
        >>> lst = ["Indrajit Ghosh", "RS Hostel", "ISI Bangalore"]
        >>> _add_texbackslash_to_list(lst)
            r"Indrajit Ghosh\\RS Hostel\\ISI Bangalore"
        """
        fine_lst = []
        for e in lst:
            if e != "":
                fine_lst.append(e)
        
        return "\\\\".join(fine_lst)
    
    @staticmethod
    def _add_comma_to_list(lst:list, _and:bool=True):
        """
        This function accepts a list and add `, ` in between each of its elements.

        Parameter(s):
        -------------
            `lst`: `list`

        Returns:
        --------
            `str`

        Example:
        --------
        >>> lst = ["Indrajit Ghosh", "RS Hostel", "ISI Bangalore"]
        >>> _add_texbackslash_to_list(lst)
            r"Indrajit Ghosh, RS Hostel and ISI Bangalore"
        """
        fine_lst = []
        for e in lst:
            if e != "":
                fine_lst.append(e)
        if len(fine_lst) == 1:
            return fine_lst[0]
        
        if not _and:
            return ", ".join(fine_lst)
        
        return ", ".join(fine_lst[:-1]) + " and " + fine_lst[-1]
    
    @staticmethod
    def join_authors(lst_authors:list):
        """
        Joins the list of authors and return appropriate `str`

        Parameter:
        ----------
            `list[Author(), ..., Author()]`

        Returns:
        -------
            `str`
        """
        return ", ".join([ath._name for ath in lst_authors])
    


class TexPackage:
    """
    A class to represent a `LaTeX` Package

    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    """
    def __init__(
            self, 
            name, 
            options:list=None,
            comment:str=None,
            associated_cmds=None
    ):
        
        if isinstance(name, str):
            self._name = name
        elif isinstance(name, list):
            self._name = ",".join(name)
        else:
            raise TypeError(
                f"The `name` attr of an {self.__class__.__name__} object \ can be of type `str` or `list`.\n"
            )
        
        self._options = (
            ",".join(options) 
            if options is not None
            else ""
        )
        self._comment = (
            comment
            if comment
            else ""
        )
        if associated_cmds is not None:
            if isinstance(associated_cmds, str):
                associated_cmds = [associated_cmds]
            if isinstance(associated_cmds, list):
                pass
            else:
                raise Exception("The attr `associated_cmds` of a `TexPackage` should be of type `list`.")
            
        self._associated_cmds = (
            "%\n".join(associated_cmds)
            if associated_cmds is not None
            else ""
        )


    def __str__(self):
        _pkg_str = ''

        if self._options == '':
            _pkg_str += r"\usepackage{" + self._name + r"}" + f"% {self._comment}\n"
        else:
            _pkg_str += r"\usepackage[" + self._options + r"]{" + self._name + r"}" + f"% {self._comment}\n"

        _pkg_str += self._associated_cmds

        _pkg_str = (
            _pkg_str
            if self._associated_cmds == ""
            else "\n" + _pkg_str + "\n"
        )

        return _pkg_str

    
    def __add__(self, right):
        return self.__str__() + right.__str__()
    
    def __radd__(self, left):
        if left == 0:
            return self
        if isinstance(left, str):
            return left.rstrip().__add__("\n" + self.__str__())
        


class TexFile:
    """
    A class representing a LaTeX file
    This is used to create `plainarticle`, `article`, `amsarticle` etc

    Author: Indrajit Ghosh
    Date: Jun 17, 2023

    Parameters
    ----------
    tex_compiler : :class:`str`
        The TeX compiler to be used, e.g. ``latex``, ``pdflatex`` or ``lualatex``

    output_format : :class:`str`
        The output format resulting from compilation, e.g. ``.dvi`` or ``.pdf``

    documentclass : :class:`str`
        The command defining the documentclass, e.g. ``\\documentclass[11pt,a4paper]{amsart}``

    pre_doc_commands : :class:`str`
        Text to be inserted at the very begining of the file, 
        e.g. ``\\newcommand{\Author}{Indrajit Ghosh}``

    preamble : :class:`str`
        The document's preamble, i.e. the part between ``\\documentclass`` and ``\\begin{document}``

    post_doc_commands : :class:`str`
        Text (definitions, commands) to be inserted at right after ``\\begin{document}``, 
        e.g. ``\\maketitle``

    body_text : :class:`str`
        Texts in between `post_doc_commands` and `end_text`
        e.g. "This is my first LaTeX document."

    end_text : :class:`str`
        This is mainly for `bibliography` related texts (in any) in the TeX file
        This text is added just before "\\end{document}"

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

    default_tex_compiler = "pdflatex"
    default_output_format = ".pdf"

    default_documentclass = r"\documentclass[12pt,twoside]{article}"
    default_pre_doc_commands = "\\newcommand{\\Title}{A \\LaTeX\ file}%\n" + \
                                "\\newcommand{\\Author}{Indrajit Ghosh}%\n"
    default_preamble = r"""
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage[top=1 in,bottom=1in, left=1 in, right=1 in]{geometry}
"""
    default_post_doc_commands = "\\title{\Title}\n\\author{\Author}\n\\maketitle"
    default_body_text = "\nYourTextHere\n"
    default_end_text = ""

    default_filename = "untitled"                                     
    default_file_extension = ".tex"
    default_author = "Indrajit Ghosh"


    def __init__(
            self,
            tex_compiler:str=None,
            output_format:str=None,
            documentclass:str=None,
            pre_doc_commands:str=None,
            preamble:str=None,
            post_doc_commands:str=None,
            body_text:str=None,
            end_text:str=None,
            filename:str=None,
            file_extension:str=None,
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

        self._pre_doc_commands = (
            pre_doc_commands
            if pre_doc_commands is not None
            else TexFile.default_pre_doc_commands
        )

        self._preamble = (
            preamble
            if preamble is not None
            else TexFile.default_preamble
        )

        self._post_doc_commands = (
            post_doc_commands
            if post_doc_commands is not None
            else TexFile.default_post_doc_commands
        )

        self._body_text = (
            body_text
            if body_text is not None
            else TexFile.default_body_text
        )

        self._end_text = (
            end_text
            if end_text is not None
            else TexFile.default_end_text
        )

        self._filename = (
            filename
            if filename is not None
            else TexFile.default_filename
        )

        self._file_extension = (
            file_extension
            if file_extension is not None
            else TexFile.default_file_extension
        )

        self._author = (
            author
            if author is not None
            else TexFile.default_author
        )

        self._classfile = classfile

        if self._classfile:
            self._documentclass = self._preamble = self._post_doc_commands = \
                self._pre_doc_commands = self._output_format = self._end_text = \
                                            self._tex_compiler = ''

        self._rebuild()

    def _rebuild(self):
        """
        Rebuilds the entire TeX template text from ``\\documentclass`` to 
        ``\\end{document}`` according to all settings and choices.
        """

        _fileinfo = [
            f"{self._filename}{self._file_extension}",
            f"Author(s): {self._author}",
            f"Date: {TODAY}"
        ]
        
        self._fileinfo = self._add_dotted_lines(
            heading=_fileinfo,
            symbol="%"
        )

        _tex_directive_compiler = (
            f"% !TEX TS-program = {self._tex_compiler}\n"
            if self._tex_compiler
            else ''
        )
        
        self.body = _tex_directive_compiler + self._fileinfo
    
        if not self._classfile:
            self.body += (
                "\n"
                + self._documentclass
                + "%\n%\n"
                + self._add_dotted_lines(
                    heading="Pre Document Commands",
                    msg=self._pre_doc_commands,
                    symbol='-',
                    factor=60
                )
                +"%\n"
                + self._add_dotted_lines(
                    heading="Preamble",
                    msg=self._preamble,
                    symbol='-',
                    factor=60
                )
                + "%\n%\n"
                + r"\begin{document}"
                + "%\n"
                + "%\n"
                + self._add_dotted_lines(
                    heading="Post Document Commands",
                    msg=self._post_doc_commands,
                    symbol='-',
                    factor=60
                )
                + "%\n"
                + self._add_dotted_lines(
                    heading="Body Text",
                    msg=self._body_text,
                    symbol='-',
                    factor=60
                )
                + "%\n\n"
                + self._add_dotted_lines(
                    heading="End Text",
                    msg=self._end_text,
                    symbol='-',
                    factor=60
                )
                + "\n\n"
                + r"\end{document}"
                + "%\n"
            )
        else:
            self.body += self._body_text + "%\n\n"

        self.body += self._add_dotted_lines(
            heading=f"End of `{self._filename}{self._file_extension}`",
            symbol="%"
        )

    @staticmethod
    def _add_dotted_lines(
        heading:str, msg:str=None, symbol:str="%", factor:int=70, _tex=True
    ):
        """
        This function returns lines to the `msg`

        Attributes:
        -----------
            `heading`: `list` or `str`
            `msg` : `str` : Optional
        
        Example
        --------
        >>> TexFile._add_dotted_lines(msg="Here is Text", heading="Hello World!)

                %--------------------------------------------%
                %                Hello World!     # heading           
                %--------------------------------------------%

                Here is Text # msg

                %--------------------------------------------%
        """
        _factor = factor
        _line = "%" + str(symbol) * _factor + "%"
        _tex_symbol = "%" if _tex else ''

        if isinstance(heading, list):
            heading = "\n%".join([el.center(_factor) for el in heading])

        _head = (
            "\n"
            + _line
            + "\n"
            + _tex_symbol + heading.center(_factor)
            + "\n"
            + _line
        )
        if msg is not None:
            _tail = (
                "\n\n"
                + msg
                + "\n\n"
                + _line
                + "\n"
            )

            return _head + _tail + "\n"
        
        return _head + "\n"


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
            "pre_doc_commands": self._pre_doc_commands,
            "preamble": self._preamble,
            "post_doc_commands": self._post_doc_commands,
            "body_text": self._body_text,
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
        self._body_text += "\n" + txt + "\n"
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
        self._rebuild()

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
    
    @staticmethod
    def tex_hash(expression:str):
        """
        Returns the `sha256` hash of `expression`
        """
        id_str = str(expression)
        hasher = hashlib.sha256()
        hasher.update(id_str.encode())

        # Truncating at 16 bytes for cleanliness
        return hasher.hexdigest()[:16]
    

    def _compile(self, tex_dir:Path=None, _open:bool=False):
        """
        Compiles the tex file inside the dir `tex_dir`

        Returns:
        --------
            `Path` of the output .pdf or .dvi

            pdflatex -halt-on-error <tex_file>
        """
        tex_dir = (
            TEX_DIR
            if tex_dir is None
            else Path(tex_dir)
        )

        # Write the TexFile inside `tex_dir`
        if not tex_dir.exists():
            tex_dir.mkdir()

        _texfilepath = self.write(tex_dir=tex_dir)

        # Change the directory
        os.chdir(tex_dir)

        # Compile TeX
        res = subprocess.run(
            [
                self._tex_compiler, '--halt-on-error', _texfilepath
            ],
            stdout=subprocess.PIPE
        )

        # Output file
        output = _texfilepath.with_suffix(self._output_format)
        _log_file = _texfilepath.with_suffix(".log")

        if res.returncode != 0:
            _print_tex_error_from_log(
                log_file=_log_file,
                tex_compiler=self._tex_compiler
            )
            
        else:
            if _open:
                open_file(output)

            return output
    


class TexEnvironment:
    """
    TODO: A class representing `LaTeX` environment

    Author: Indrajit Ghosh
    Date: 
    """
    pass


class TexTable:
    """
    TODO: A class representing `LaTeX` table

    Author: Indrajit Ghosh
    Date: 

    Reference(s):
    -------------
        [1] https://github.com/astanin/python-tabulate/blob/master/tabulate/__init__.py
        [2] https://github.com/JelteF/PyLaTeX/blob/master/pylatex/table.py
    """
    pass

class TexMatrix:
    """
    TODO: A class representing `LaTeX` matrix

    Author: Indrajit Ghosh
    Date:

    Reference:
    ----------
        [1] https://github.com/indrajit912/LinearAlgebra/blob/master/linear_algebra.py
    """
    pass


class TexSection(TexFile):
    """
    A class representing a `LaTeX` section

    Author: Indrajit Ghosh
    Date: Aug 1, 2023
    """

    def __init__(
            self,
            heading:str="Untitled \\LaTeX\\ Section",
            content:str="",
            filename:str=None,
            author:str=None
    ):
        
        self._heading:str = heading
        self._content:str = content

        super().__init__(
            filename=filename,
            author=author,
            body_text=self.__str__(),
            classfile=True
        )

    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, new_content:str):
        self._content = new_content
        super().__setattr__("body_text", self.__str__())

    
    def add_subsection(self, heading:str, text:str):
        """
        Adds a subsection to the Section
        """
        self._content += (
            "\n\n\\subsection{"
            + heading
            + "} %\n" 
            + text 
            + "\n"
        )
        super().__setattr__("body_text", self.__str__())


    def __str__(self):
        return (
            "\\section{"
            + self._heading
            + "} %\n" 
            + self._content 
            + "\n\n"
        )
    
    


class Preamble(TexFile):
    """
    TODO: Improve this class
    A class representing a `TeX` preamble
    This is a `TexFile(classfile=True)` object

    Author: Indrajit Ghosh
    Date: Jul 21, 2023

    Parameter(s):
    -------------
        `packages` : `list[Package(), ..., Package()]`
        `theorem_styles` : `str`
        `custom_commands`: `str`
    """
    def __init__(
            self, 
            packages:list=None,
            theorem_styles:str=None,
            custom_commands:str=None,
            filename:str=None, 
            **kwargs
    ):

        _filename = (
            "preamble" if filename is None
            else filename
        )

        _packages:list = (
            packages if packages is not None
            else self._default_amsart_packages()
        )

        _thm_styles = (
            theorem_styles if theorem_styles is not None
            else self._default_ams_theorem_styles()
        )

        _cmds = (
            custom_commands if custom_commands is not None
            else self._default_ams_commands()
        )

        _preamble_body_text = TexFile._add_dotted_lines(
            heading="Required Packages",
            msg=sum(_packages),
            symbol='.',
            factor=60
        )

        _preamble_body_text += TexFile._add_dotted_lines(
            heading="Theorem Styles",
            msg=_thm_styles,
            symbol='.',
            factor=60
        )

        _preamble_body_text += TexFile._add_dotted_lines(
            heading="Custom Commands & Macros",
            msg=_cmds,
            symbol='.',
            factor=60
        )

        super().__init__(
            tex_compiler='',
            output_format='.tex',
            classfile=True,
            body_text=_preamble_body_text,
            filename=_filename,
            **kwargs
        )

    @staticmethod
    def _default_amsart_packages():
        """
        Returns LaTeX packages that I usually use in `amsart` doc.
        """
        return [
            TexPackage(name="inputenc", options=['utf8']),
            TexPackage(name="fontenc", options=['T1']),
            TexPackage(
                name="lmodern",
                comment="To get high quality fonts"
            ),
            TexPackage(
                name="geometry",
                options=[
                    "top=0.9in",
                    "bottom=1in",
                    "left=1in",
                    "right=1in"
                ]
            ),
            TexPackage(
                name=["amsmath", "amssymb", "amsthm", "amscd"],
                comment= "amssymb internally loads amsfonts"
            ),
            TexPackage(
            name="hyperref",
            associated_cmds=[
                r"""\hypersetup{
	pdftitle={\pdfTitle},
	pdfauthor={\pdfAuthor},
	pdfsubject={\pdfSubject},
	pdfcreationdate={\pdfCreationDate},
	pdfcreator={\pdfCreator},
	pdfkeywords={\pdfKeywords},
	colorlinks=\pdfColorLink,
	linkcolor={\pdfLinkColor},
	%    filecolor=magenta,      
	urlcolor=\pdfUrlColor,
	citecolor=\pdfCiteColor,
	pdfpagemode=UseOutlines,
}"""
            ]
        ),
        TexPackage(name="xcolor"),
        TexPackage(name="lipsum"),
        ]
    
    @staticmethod
    def _default_ams_theorem_styles():
        """
        Returns ams theorem style that I usually use.
        """
        return r"""\theoremstyle{plain} %% This is the default, anyway
\begingroup % Confine the \theorembodyfont command
%\theorembodyfont{\sl}
\newtheorem{bigthm}{Theorem} % Numbered separately, as A, B, etc.
\newtheorem{thm}{Theorem}[section] % Numbered within each section
\newtheorem{cor}[thm]{Corollary} % Numbered along with thm
\newtheorem{lem}[thm]{Lemma} % Numbered along with thm
\newtheorem{prop}[thm]{Proposition} % Numbered along with thm
\endgroup

%%% We need to do the following outside of any group,
%%% since it’s not \global:
\renewcommand{\thebigthm}{\Alph{bigthm}} % Number as "Theorem A."

\theoremstyle{definition}
\newtheorem{defn}[thm]{Definition} % Numbered along with thm
\theoremstyle{remark}
\newtheorem{rem}[thm]{Remark} % Numbered along with thm
\newtheorem{ex}[thm]{Example} % Numbered along with thm
\newtheorem{notation}{Notation}
\renewcommand{\thenotation}{} % to make the notation environment unnumbered
\newtheorem{terminology}{Terminology}
\renewcommand{\theterminology}{} % to make the terminology environment unnumbered

%%% The following causes equations to be numbered within sections:
\numberwithin{equation}{section}

\renewcommand\qedsymbol{$\blacksquare$} % To change the qed symbol
"""
    
    @staticmethod
    def _default_ams_commands():
        """
        Commands that I usually use in my documents
        """
        return r"""
% Here I define a macro \mathcolor for coloring text in math mode.
\makeatletter
\def\mathcolor#1#{\@mathcolor{#1}}
\def\@mathcolor#1#2#3{%
	\protect\leavevmode
	\begingroup
	\color#1{#2}#3%
	\endgroup
}
\makeatother

% Celling and Floor function
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}

% Operations
\newcommand{\N}{\mathbb{N}}
\newcommand{\quotes}[1]{\textquotedblleft #1\textquotedblright}
\newcommand{\tensor}{\otimes}
"""


def main():
    _dir = Path.home() / "Desktop" / "newart"

    texfile = TexFile()
    texfile.add_to_document("Hello There I am Indrajit Ghosh")

    texfile._compile(
        tex_dir=_dir,
        _open=True
    )



if __name__ == '__main__':
    main()