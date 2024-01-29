# A module for LaTeX
#
# Author: Indrajit Ghosh
# Created On: Jun 17, 2023
# Modified On: Jul 20, 2023; Jan 29, 2024
#

from datetime import datetime
import copy, re, hashlib, subprocess, os, sys
from pathlib import Path
from .utils import open_file, _print_tex_error_from_log

TEX_DIR = Path(__file__).parent / "tex_dir"

__all__ = [
    "Email",
    "Author", 
    "TexFile",
    "TexPackage",
    "TexEnvironment",
    "TexTable", 
    "TexSection", 
    "Frame",
    "BeamerSection",
    "Preamble"
]

TODAY = datetime.now().strftime('%b %d, %Y') # Today's date in `Mmm dd, YYYY`

class Email(str):
    """
    A class representing an email address with LaTeX formatting capabilities.

    This class inherits from the built-in str class and extends it to provide
    LaTeX-formatted representations of email addresses.

    Args:
        email_id (str): The email address.
        texttt (bool, optional): If True, wrap the email in \texttt{} in LaTeX formatting.

    Example:
        >>> email = Email("indrajit_ghosh@gmail.com", texttt=True)
        >>> print(email)
        r"\texttt{indrajit\_ghosh@gmail.com}"
    """

    def __new__(cls, email_id, texttt=False):
        """
        Create a new Email instance.

        Args:
            email_id (str): The email address.
            texttt (bool, optional): If True, wrap the email in \texttt{} in LaTeX formatting.

        Returns:
            Email: The Email instance.
        """
        instance = super(Email, cls).__new__(cls, email_id)
        instance.texttt = texttt
        return instance

    def __str__(self):
        """
        Get the LaTeX-formatted representation of the email.

        Returns:
            str: The LaTeX-formatted email.
        """
        escaped_email = TexFile.latex_escape(self)
        if self.texttt:
            return r"\texttt{" + escaped_email + "}"
        else:
            return escaped_email

class Author:
    """
    A class representing an Article author
    
    Author: Indrajit Ghosh
    Date: Jul 20, 2023
    Modified On: Aug 23, 2023


    Parameters:
    -----------
    name : str, optional
        Name of the author.
    department : str, optional
        Department of the author.
    institute : str, optional
        Institute of the author.
    address : list, optional
        Address of the author as a list of strings.
    email : str, optional
        Email address of the author.
    current_address : list, optional
        Current address of the author as a list of strings.
    support : str, optional
        Support information for the author.

    Example:
    --------
    author = Author(name="John Doe", institute="University X")
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
        name: str = None,
        department: str = None,
        institute: str = None,
        address: list = None,
        email: str = None,
        current_address: list = None,
        support: str = None
    ):
        """
        Initialize an Author instance.
        """
        self._name = (
            name
            if name is not None
            else self._default_name
        )
        self._dept: str = (
            department
            if department is not None
            else self._default_dept
        )
        self._institute: str = (
            institute
            if institute is not None
            else self._default_institute
        )
        self._addr: list = (
            address
            if address is not None
            else self._default_addr
        )
        _fulladdr = [self._dept, self._institute] + self._addr
        self._amsAddrTeX: str = self._add_comma_to_list(_fulladdr)
        self._email: str = (
            None
            if email is None
            else TexFile.latex_escape(email)
        )
        self._curr_addr: list = current_address
        self._currAddrTeX = (
            self._add_comma_to_list(self._curr_addr)
            if self._curr_addr is not None
            else None
        )
        self._support = support

    @property
    def name(self):
        """Get or set the author's name."""
        return self._name
    
    @name.setter
    def name(self, new: str):
        self._name = new

    @property
    def department(self):
        """Get or set the author's department."""
        return self._dept
    
    @department.setter
    def department(self, new: str):
        self._dept = new
    
    @property
    def institute(self):
        """Get or set the author's institute."""
        return self._institute

    @institute.setter
    def institute(self, new: str):
        self._institute = new

    @property
    def address(self):
        """Get or set the author's address."""
        return self._addr
    
    @address.setter
    def address(self, new: list):
        self._addr = new

    @property
    def email(self):
        """Get or set the author's email."""
        return self._email
    
    @email.setter
    def email(self, new: str):
        self._email = new

    @property
    def current_address(self):
        """Get or set the author's current address."""
        return self._curr_addr
    
    @current_address.setter
    def current_address(self, new: list):
        self._curr_addr = new

    @property
    def support(self):
        """Get or set the author's support information."""
        return self._support
    
    @support.setter
    def support(self, new: str):
        self._support = new

    @staticmethod
    def _add_texlinebreak_to_list(lst: list):
        """
        Add `\\` between elements of a list and return as a string.
        
        Parameters:
        -----------
        lst : list
            List of strings.

        Returns:
        --------
        str
            Joined string with '\\\\' between elements.
        
        Example:
        --------
        lst = ["Indrajit Ghosh", "RS Hostel", "ISI Bangalore"]
        _add_texlinebreak_to_list(lst)
        # Output: "Indrajit Ghosh\\\\RS Hostel\\\\ISI Bangalore"
        """
        fine_lst = [e for e in lst if e != ""]
        return "\\\\".join(fine_lst)
    
    @staticmethod
    def _add_comma_to_list(lst: list, _and: bool = True):
        """
        Add ', ' or ' and ' between elements of a list and return as a string.
        
        Parameters:
        -----------
        lst : list
            List of strings.
        _and : bool, optional
            Whether to use ' and ' before the last element, by default True.

        Returns:
        --------
        str
            Joined string with ', ', ' and ' as appropriate.

        Example:
        --------
        lst = ["Indrajit Ghosh", "RS Hostel", "ISI Bangalore"]
        _add_comma_to_list(lst)
        # Output: "Indrajit Ghosh, RS Hostel and ISI Bangalore"
        """
        fine_lst = [e for e in lst if e != ""]
        if len(fine_lst) == 1:
            return fine_lst[0]
        if not _and:
            return ", ".join(fine_lst)
        return ", ".join(fine_lst[:-1]) + " and " + fine_lst[-1]
    
    @staticmethod
    def join_authors(lst_authors: list):
        """
        Join a list of authors' names and return as a comma-separated string.
        
        Parameters:
        -----------
        lst_authors : list[Author(), ..., Author()]
            List of Author instances.

        Returns:
        --------
        str
            Comma-separated string of author names.

        Example:
        --------
        authors = [Author(name="John Doe"), Author(name="Jane Smith")]
        Author.join_authors(authors)
        # Output: "John Doe, Jane Smith"
        """
        return ", ".join([ath._name for ath in lst_authors])

class TexPackage:
    """
    A class to represent a LaTeX Package
    
    Author: Indrajit Ghosh
    Date: Jul 20, 2023

    Parameters:
    -----------
    name : str or list
        Name of the LaTeX package. If a list is provided, package names will be joined with commas.
    options : list, optional
        List of options to be passed to the package.
    comment : str, optional
        Comment or description associated with the package.
    associated_cmds : str or list, optional
        Additional LaTeX commands associated with the package.

    Example:
    --------
    package = TexPackage(name="geometry", options=["margin=1in"], comment="Set page margins")
    """
    def __init__(
            self, 
            name, 
            options: list = None,
            comment: str = None,
            associated_cmds = None
    ):
        """Initialize a TexPackage instance."""

        if isinstance(name, str):
            self._name = name
        elif isinstance(name, list):
            self._name = ",".join(name)
        else:
            raise TypeError(
                f"The `name` attribute of a {self.__class__.__name__} object can be of type `str` or `list`.\n"
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
                raise Exception("The `associated_cmds` attribute of a `TexPackage` should be of type `list`.")
            
        self._associated_cmds = (
            "%\n".join(associated_cmds)
            if associated_cmds is not None
            else ""
        )

    def __str__(self):
        """
        Return the LaTeX representation of the package.
        """
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
        """
        Concatenate the LaTeX representation of two packages or a package and a string.
        """
        return self.__str__() + right.__str__()

    def __radd__(self, left):
        """
        Concatenate the LaTeX representation of a package with a string on the left side.
        """
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
    def render_tex_template(template_path:Path, variable_dict):
        """
        TODO: Added this function late! Imeplement it throughout the project whereever applicable.

        Render a LaTeX template by replacing Python variable placeholders with actual values.

        Args:
        -----
            template_path (str): Path to the LaTeX template file.
            variable_dict (dict): Dictionary containing variable names and their corresponding values.

        Returns:
        --------
            str: Rendered LaTeX content as a string.

        Example:
        --------
            Suppose you have the following `main.tex` file
                `main.tex`

                    \documentclass{article}
                    \title{{{ title }}}
                    \author{{{ author }}}
                    \date{{{ date }}}
                    \begin{document}
                    \maketitle

                    This is a sample document authored by {{ author }} on {{ date }}.

                    \end{document}

            Then you run the following

            >>> template_path = 'demo.tex'  # Replace with the actual path to your template file
            >>> variables = {
                'author': 'John Doe',
                'title': 'My Document Title',
                'date': '2023-08-24',
            }
            >>> rendered_tex = render_tex_template(template_path, variables)

                    \documentclass{article}
                    \title{My Document Title}
                    \author{John Doe}
                    \date{2023-08-24}
                    \begin{document}
                    \maketitle

                    This is a sample document authored by John Doe on 2023-08-24.

                    \end{document}
        """
        template_path = Path(template_path).resolve()
        
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()

        for variable_name, variable_value in variable_dict.items():
            placeholder = f'{{{{ {variable_name} }}}}'
            template_content = template_content.replace(placeholder, str(variable_value))

        return template_content
    
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

        # Compile TeX
        res = subprocess.run(
            [
                self._tex_compiler,
                "-interaction=batchmode",
                "-synctex=1",
                '--halt-on-error', 
                _texfilepath
            ],
            stdout=subprocess.PIPE,
            cwd=tex_dir
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
    A class representing a LaTeX environment
    
    Author: Indrajit Ghosh
    Date: Aug 23, 2023
    """
    def __init__(self, name, content=None, options=None):
        """
        Initialize a TexEnvironment instance.
        
        Parameters:
        -----------
        name : str
            Name of the LaTeX environment.
        content : str or list, optional
            Content to be placed within the environment. If a list is 
            provided, content will be joined with line breaks.
        options : list, optional
            List of options to be passed to the environment.
        
        Example:
        --------
        environment = TexEnvironment(name="quote", content="This is a quotation.")
        """
        self._name = name
        self._options = (
            ",".join(options)
            if options is not None
            else ""
        )
        self._content = (
            "\n".join(content)
            if isinstance(content, list)
            else content
        )


    def __str__(self):
        """
        Return the LaTeX representation of the environment.
        """
        env_str = f"\\begin{{{self._name}}}"

        if self._options:
            env_str += f"[{self._options}]"

        env_str += f"\n    {self._content}\n\\end{{{self._name}}}"
        return "\n" + env_str + "\n"



class TexTable:
    """
    A class representing `LaTeX` table

    Author: Indrajit Ghosh
    Date: Aug 01, 2023

    Parameters
    ----------
    columns : list
        A list of column names for the table.
    rows : list, optional
        A list of lists representing the rows of the table. Each inner list should
        contain the values for each column in the respective row. Default is None.
    col_spec : str, optional
        The column specification for the `tabular` or `longtable` environment in LaTeX.
        Default is None, which generates "l c c c" for n columns, where n is the number
        of columns provided in the `columns` parameter.
    longtable : bool, optional
        If True, the table will be rendered using the `longtable` environment in LaTeX,
        allowing the table to span multiple pages. If False, the `tabular` environment
        will be used. Default is False.
    center : bool, optional
        If True, the table will be centered in the output. If False, the table will be
        left-aligned. Default is True.

    Attributes
    ----------
    _columns : list
        A list containing the column names of the table.
    _num_of_cols : int
        The number of columns in the table.
    _col_spec : str
        The column specification for the `tabular` or `longtable` environment in LaTeX.
    _longtable : bool
        If True, the table will be rendered using the `longtable` environment in LaTeX.
    _center : bool
        If True, the table will be centered in the output. If False, the table will be
        left-aligned.
    _rows : list
        A list of lists representing the rows of the table. Each inner list contains the
        values for each column in the respective row.
    _row_gap : str, optional
        Optional gap specification between rows in the `longtable` environment in LaTeX.
    _top_line : bool
        If True, a top horizontal line will be added to the table. Default is False.
    _bottom_line : bool
        If True, a bottom horizontal line will be added to the table. Default is False.
    _texcode : str
        The generated LaTeX code for the entire table.

    Methods
    -------
    add_row(row: list)
        Adds a new row to the table.
        
    """
    def __init__(
            self,
            columns:list,
            rows:list=None,
            col_spec:str=None,
            longtable:bool=False,
            center:bool=True,
            *,
            row_gap:str=None,
            top_line:bool=False,
            bottom_line:bool=False
    ):
        self._columns:list = columns # ["Name", "Email", "Address"]
        self._num_of_cols = len(self._columns)

        if col_spec is None:
            self._col_spec = "l " + " ".join(['c'] * (len(self._columns) - 1)) # "l c c c"
        elif len(col_spec) == 1:
            self._col_spec = " ".join([col_spec] * len(self._columns))
        else:
            self._col_spec = col_spec

        self._longtable = longtable
        self._center = center

        self._rows:list = (
            [] if rows is None
            else rows
        )

        self._row_gap = (
            row_gap
            if row_gap
            else ""
        )
        self._top_line = top_line
        self._bottom_line = bottom_line

        self._update_tex()


    def _update_tex(self):
        """
        Updates the LaTeX code for the entire table
        """
        _tex = "\n"
        _tex += (
            r"\begin{center}" + "%\n" 
            if self._center
            else ''
        )

        _tex += (
            r"\begin{longtable}{%s}\hline" % self._col_spec + "%\n"
            if self._longtable
            else 
            r"\begin{tabular}{%s}" % self._col_spec + "%\n"
        )

        _top_line_str = (
            "\n    " + r"\hline%"
            if self._top_line
            else ''
        )
        _tex += _top_line_str + "\n"

        _tex += (
            "    "
            + " & ".join(self._columns) + r"\\%"
            + "\n    "
            + r"\hline\hline%"
            + "\n\n"
        )

        for row in self._rows:
            _gap_str = (
                "[" + self._row_gap + "]"
                if self._row_gap != ''
                else ''
            )
            _tex += "    " + " & ".join(str(val) for val in row) + r"\\" + _gap_str + "%\n"

        _bottom_line_str = (
            "    " + r"\hline%" + "\n"
            if self._bottom_line
            else ''
        )
        _tex += _bottom_line_str + "\n"

        _tex += f"\\end{{longtable}}%\n" if self._longtable else "\\end{tabular}%\n"

        _tex += (
            r"\end{center}%"
            if self._center
            else ''
        )
        _tex += "\n"

        self._texcode = _tex


    def __str__(self):
        self._update_tex()
        return self._texcode
    

    def add_row(self, row:list):
        """
        Adds a row to `self._rows`
        """
        self._rows.append(row)


class TexFigure:
    """
    TODO: A class representing `LaTeX figure`

    Author: Indrajit Ghosh
    Date: Aug 02, 2023


        \begin{figure}[htbp]
            \centering
            \includegraphics[<--->] # command from the `graphicx` package
            \caption{<--->}
            \label{<--->}
        \end{figure}

    Options in \begin{figure}[ ]:
    ------------------------------

    h: Place the figure "here" at the current position in the text where the 
    figure environment appears. If there is enough space on the page, the 
    figure will be placed here.

    t: Place the figure at the "top" of a page, above any text that appears on the page.

    b: Place the figure at the "bottom" of a page, below any text that appears on the page.

    p: Place the figure on a separate "page" that contains only floating elements such 
    as figures and tables.

    !: Override the internal parameters of LaTeX to force the figure to be placed, even if 
    the specified location is not ideal according to its usual placement rules.

    The options can be combined, and the order matters. For example, using [htbp] will tell 
    LaTeX to try placing the figure "here," then at the "top" of a page, then at the "bottom," 
    and finally on a "separate page."


    Options in \includegraphics[ ]:
    -------------------------------
    options:

    `width`: Sets the width of the inserted image. 
        For example, \includegraphics[width=0.8\textwidth]{image.jpg} will set 
        the width of the image to 80% of the text width.
    
    `height`: Sets the height of the inserted image. 
        For example, \includegraphics[height=4cm]{image.jpg} will set the 
        height of the image to 4 centimeters.
    
    `scale`: Scales the image by a given factor. 
        For example, \includegraphics[scale=0.5]{image.jpg} will scale the 
        image to half its original size.
    
    `angle`: Rotates the image by a given angle in degrees. 
        For example, \includegraphics[angle=45]{image.jpg} will rotate the 
        image by 45 degrees.
    
    `trim`: Crops the image by specifying the left, bottom, right, and top 
        trimming values in the format trim = {left} {bottom} {right} {top}. 
        For example, \includegraphics[trim=10mm 20mm 10mm 30mm]{image.jpg} will 
        remove 10mm from the left, 20mm from the bottom, 10mm from the right, and 
        30mm from the top of the image.
    
    `clip`: Clips the image to the dimensions specified by trim. This option is 
        used in conjunction with the trim option. 
        For example, \includegraphics[trim=10mm 20mm 10mm 30mm, clip]{image.jpg} 
        will trim and clip the image as specified.
    
    `keepaspectratio`: Maintains the aspect ratio of the image when resizing. 
        For example, \includegraphics[width=5cm, keepaspectratio]{image.jpg} will 
        set the width to 5 centimeters while preserving the aspect ratio.
    
    `natwidth` and `natheight`: Specifies the natural width and height of the image. 
        These options are used to override the values stored in the image file. 
        For example, \includegraphics[natwidth=200pt, natheight=150pt]{image.jpg} will 
        set the natural width to 200 points and the natural height to 150 points.
    
    `draft`: Replaces the image with a placeholder box of the same size. This option is 
        useful for faster compilation during the draft phase when you don't want to 
        include the actual images.

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
    A class representing `LaTeX` section

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
            "\n\n"
            "\\section{"
            + self._heading
            + "} %\n" 
            + self._content 
            + "\n\n"
        )
    

class Frame:
    """
    A class representing a `Frame` in a TeX Beamer Section

    Author: Indrajit Ghosh
    Date: Jan 29, 2024
    """
    def __init__(self, title:str, text:str=''):
        self._title = title
        self._text = text

    def __str__(self):
        return (
            "\n"
            + r"\frame %"
            + "\n"
            + r"{%"
            + "\n"
            + r"\frametitle{"
            + self._title
            + r"}%"
            + "\n\n"
            + self._text
            + "\n\n"
            + r"}%"

        )
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title:str):
        self._title = new_title

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, new_text):
        self._text = new_text

class BeamerSection(TexFile):
    """
    A class representing a LaTeX Beamer Section
    This is a `TexFile(classfile=True)` object

    Author: Indrajit Ghosh
    Date: Jan 29, 2024
    """
    def __init__(
            self,
            heading:str="Untitled Beamer Section",
            filename:str=None,
            author:str=None
    ):
        
        self._heading:str = heading
        self._content = ''

        super().__init__(
            filename=filename,
            author=author,
            body_text=self.__str__(),
            classfile=True
        )

    
    def __str__(self):
        return (
            "\n\n"
            "\\section{"
            + self._heading
            + "} %\n" 
            + self._content 
            + "\n\n"
        )
    
    def add_frame(self, frame:Frame):
        """
        Adds a frame to the section
        """
        if isinstance(frame, Frame):
            self._content += frame.__str__() + "\n"
            super().__setattr__("body_text", self.__str__())
        else:
            raise TypeError("Only `Frame` type object can be added to BeamerSection!")


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