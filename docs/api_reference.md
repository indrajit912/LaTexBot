# LaTexBot API Reference

Welcome to the LaTexBot API Reference! This guide provides detailed information about the classes, methods, and functions available in the LaTexBot project. Use this reference to understand the functionality of different components and how to use them in your code.

## Table of Contents

- [Introduction](#introduction)
- [Classes](#classes)
  - [TexFile](#texfile-class)
  - [PlainArticle](#plainarticle-class)
  - [Article](#article-class)
  - [AmsArticle](#amsarticle-class)
  - [Others](#other-classes)
- [Functions and Utilities](#functions-and-utilities)
  - [latex_bot.utils](#latex_bot-utils-module)
  - [latex_bot.tex_templates](#latex_bot-tex_templates-module)
- [Example Usage](#example-usage)

## Introduction

LaTexBot provides a range of classes and utilities to simplify the process of generating LaTeX documents. This reference guide offers insights into the functionality of these components and how they can be used to create and customize documents.

## Classes

### TexFile Class

The `TexFile` class is the base class for all LaTeX document types. It provides methods and attributes for setting up a LaTeX document, adding content, and generating the output.

#### Attributes

- `title`: The title of the document.
- `project_dir`: The directory where the LaTeX files will be created.
- `sections`: A list of sections in the document.
- ...

#### Methods

- `add_section(title)`: Add a new section to the document.
- `add_text(content)`: Add plain text content to the document.
- `show_output()`: Display the current document structure.
- `create()`: Generate the LaTeX output.


## Classes

### PlainArticle Class

The `PlainArticle` class provides a template for creating plain articles in LaTeX.

#### Example

```python
from latex_bot import PlainArticle

document = PlainArticle(title="My Plain Article", project_dir="path/to/project")
document.add_section("Introduction")
document.add_text("This is the introduction section.")
document.create()
```


### Article Class

The `Article` class provides a template for creating regular articles in LaTeX.

#### Example

```python
from latex_bot import Article

document = Article(title="My Regular Article", project_dir="path/to/project")
document.add_section("Introduction")
document.add_text("This is the introduction section.")
document.create()
```


### AmsArticle Class
The AmsArticle class provides a template for creating articles using the AMS (American Mathematical Society) format.

#### Example
```python
from latex_bot import AmsArticle

document = AmsArticle(title="My AMS Article", project_dir="path/to/project")
document.add_section("Abstract")
document.add_text("This is the abstract section.")
document.create()
```

## Others
Describe other classes available in your project.

### Functions and Utilities
`latex_bot.utils` Module
This module provides utility functions for working with LaTeX documents.

#### Example
```python
from latex_bot.utils import format_author

author = format_author("John Doe")
print(author)  # Outputs: \author{John Doe}
```

## Example Usage

For more detailed examples of using these classes and utilities, refer to the [Examples](examples.md) section.

[Back to Home](../README.md)
