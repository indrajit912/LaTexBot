# Tests will be performed here.
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023

from latex_bot import *
from pprint import pprint

def main():

    art = PlainArticle(
        title="\\TeX\ Template Article",
        authors=[IndraAMS.indrajit],
        project_dir=Path.home() / "Desktop" /"new_article",
    )

    art.add_text(
        r"Here are some Multiline texts to be added to the documents",
        noindent=True
    )

    art.add_section(
        data=TexSection(
            heading="My New Section",
            content="I'll mainly focus on how \\LaTeX can be used through Python."
        )
    )

    row_data = [
        ["John Doe", 30, "Engineer"],
        ["Jane Smith", 28, "Scientist"]
    ]
    table = TexTable(
        columns=["Name", "Age", "Occupation"],
        rows=row_data,
        row_gap="2pt",
        longtable=True
    )
    table.add_row(["Michael Johnson", 35, "Teacher"])

    art.add_table(table)

    art.add_paragraph(
        r"""However, it's important to note that for a dictionary key to be valid, it must be hashable. 
In Python, hashable objects are those that have a hash value that does not 
change during their lifetime and can be compared for equality. 
Immutable data types like integers, strings, floats, and tuples are hashable, while mutable data 
types like lists and dictionaries are not hashable and cannot be used as keys in a dictionary.
"""
    )

    art.add_package(
        TexPackage(name="longtable")
    )

    # art._amsartstyle = True

    art.add_reference(
        reference=r"""
@article{smith2020article,
  author = {Smith, John and Johnson, Jane},
  title = {An Example Article},
  journal = {Journal of Examples},
  year = {2020},
  volume = {10},
  pages = {1-10},
}
"""
    )


    art.create()



if __name__ == '__main__':
    main()
    