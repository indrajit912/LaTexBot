# LaTexBot

## Project Description

LaTexBot is a Python project developed by Indrajit Ghosh to simplify the process of writing and compiling LaTeX documents. The project provides a collection of classes that enable users to produce various LaTeX document templates with ease.

## Features

- Write and compile LaTeX documents effortlessly.
- Ready-to-use classes such as `TexFile`, `PlainArticle`, `Article`, `AmsArticle`, and more.
- Customize templates for different types of documents.
- Easily integrate LaTeX code into your Python project.

## Dependencies
This project requires a LaTeX distribution to be installed on your system. A LaTeX distribution is necessary to compile and generate documents from LaTeX source code. You can choose from the following popular LaTeX distributions:

- **TeX Live:** TeX Live is a cross-platform, comprehensive distribution that provides a wide range of packages and tools for LaTeX typesetting. It's available for various operating systems including Windows, macOS, and Linux. You can download TeX Live from their official website: [TeX Live](https://www.tug.org/texlive/)

- **MiKTeX:** MiKTeX is a LaTeX distribution for Windows, known for its ease of installation and package management capabilities. It provides a user-friendly interface for package installation and updates. You can download MiKTeX from their official website: [MiKTeX](https://miktex.org/)

- **MacTeX:** MacTeX is a distribution specifically designed for macOS, providing everything you need to work with LaTeX on a Mac. It includes various tools and editors that integrate well with the macOS environment. You can download MacTeX from their official website: [MacTeX](https://www.tug.org/mactex/)

Please make sure to install one of these LaTeX distributions before using this project to ensure that you can compile the LaTeX source code and generate the desired documents.


## Installation

Open a new terminal window and `cd` to where you want to install `LaTexBot`. Then follow the steps below:

1. Clone the project from GitHub using the following command:

```
git clone https://github.com/indrajit912/LaTexBot.git
```

2. Change into the project directory:

```
cd LaTexBot
```

3. (Optional but Recommended) Create virtualenv (if you don't have `virtualenv` in your python distribution, install it using `pip`).

```
virtualenv env
```
4. (Optional, if you followed 3.) Activate the `virtualenv`

```
source env/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Check whether everything is installed correctly by running the following script staying in the root directory `LaTexBot/`:
```
python3 examples/example_plain_article.py
```
If you see a `pdf` then everything is working as fine!

## Usage

1. Import the desired class from the `LaTexBot` package into your Python script.

2. Instantiate the class and customize the LaTeX document as needed.

3. Use the provided methods to write and compile the document.

```python
from LaTexBot import TexFile, PlainArticle

# Create a PlainArticle document
document = PlainArticle(
    title="My LaTeX Document",
    project_dir="home/Desktop/new_plain_art" # Change with a proper path.
)

# Add sections, content, and other elements
document.add_section("Introduction")
document.add_text("This is the introduction section.")

# Create the document
document.show_output()
document.create()
```

# Documentation
For detailed documentation and examples, please refer to the LaTexBot Wiki (*Will be updated soon!*).

# Contributions
Contributions to LaTexBot are welcome! If you find a bug, have a feature request, or want to contribute improvements, please submit a pull request or open an issue on [GitHub](https://github.com/indrajit912/LaTexBot.git).

# Contact
- Author: **Indrajit Ghosh**
- Email: indrajitghosh912@gmail.com
- GitHub: [indrajit912](https://github.com/indrajit912)

# License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.