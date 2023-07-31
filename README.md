# LaTexBot

<!-- ![LaTexBot Logo](https://example.com/latexbot_logo.png) -->

## Project Description

LaTexBot is a Python project developed by Indrajit Ghosh to simplify the process of writing and compiling LaTeX documents. The project provides a collection of classes that enable users to produce various LaTeX document templates with ease.

## Features

- Write and compile LaTeX documents effortlessly.
- Ready-to-use classes such as `TexFile`, `PlainArticle`, `Article`, `AmsArticle`, and more.
- Customize templates for different types of documents.
- Easily integrate LaTeX code into your Python project.

## Installation

1. Clone the project from GitHub using the following command:

```
git clone https://github.com/indrajit912/LaTexBot.git
```

2. Change into the project directory:

```
cd LaTexBot
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Import the desired class from the `LaTexBot` package into your Python script.

2. Instantiate the class and customize the LaTeX document as needed.

3. Use the provided methods to write and compile the document.

```python
from LaTexBot import TexFile, PlainArticle

# Create a PlainArticle document
document = PlainArticle("my_document.tex", title="My LaTeX Document")

# Add sections, content, and other elements
document.add_section("Introduction")
document.add_text("This is the introduction section.")

# Write and compile the document
document.write_tex()
document.compile_pdf()
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
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as per the terms of the license.