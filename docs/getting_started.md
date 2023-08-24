# Getting Started with LaTexBot

Welcome to LaTexBot! This guide will walk you through the steps to get started with using and contributing to this project.

## Installation

Before you can use LaTexBot, you need to have Python 3.x and a LaTeX distribution installed on your system. Follow these steps to set up your environment:

1. **Python 3.x:** If you don't have Python 3.x installed, you can download it from the official Python website: [Python Downloads](https://www.python.org/downloads/).

2. **LaTeX Distribution:** A LaTeX distribution is required to compile and generate documents from LaTeX source code. You have several options:

   - **TeX Live:** TeX Live is a comprehensive distribution available for various operating systems, including Windows, macOS, and Linux. Download it from [TeX Live](https://www.tug.org/texlive/).

   - **MiKTeX:** MiKTeX is a LaTeX distribution for Windows known for its easy installation and package management. Get it from [MiKTeX](https://miktex.org/).

   - **MacTeX:** MacTeX is designed for macOS and includes tools and editors. Download it from [MacTeX](https://www.tug.org/mactex/).

## Installation Steps

Follow these steps to set up LaTexBot on your system:

1. Clone the project repository from GitHub using the following command:
    ```
    git clone https://github.com/indrajit912/LaTexBot.git
    ```

2. Change into the project directory:
    ```
    cd LaTexBot
    ```

3. (Optional but Recommended) Create a virtual environment:
    ```
    virtualenv env
    ```

4. (Optional, if you followed 3.) Activate the virtual environment:
    ```
    source env/bin/activate
    ```


5. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```


## Basic Usage

Now that you have LaTexBot set up, you can start using it to create and compile LaTeX documents. Here's a simple example:

1. Import the desired class (e.g. `PlainArticle`) from the `latex_bot` package into your Python script.

2. Create an instance of the class and provide necessary information like title and project directory.

3. Add sections, content, and other elements to the document.

4. Use the provided methods to show the output and create the document.

For more detailed usage examples and documentation, please refer to the [Usage Guide](usage_guide.md).

## Contributing

If you're interested in contributing to LaTexBot, please check out our [Contributing Guidelines](contributing.md) for more information on how to get involved and submit contributions.

We hope you enjoy using LaTexBot to simplify your LaTeX document creation process!

[Back to Home](../README.md)

