# Tests will be performed here for PlainArticle.
#
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023
# Modified On: Aug 23, 2023
#
# Test this from the `root_dir` using the following cmd:
#       root_dir = Path(__file__).parent.parent
#       `env/bin/python -m unittest tests.test_plain_article`
#


import unittest
from latex_bot import *

class TestPlainArticle(unittest.TestCase):
    
    def setUp(self):
        # Create an instance of PlainArticle for testing
        self.article = PlainArticle(
        title="\\TeX\ Template Article",
        authors=[IndraAMS.indrajit],
        project_dir=Path.home() / "Desktop" /"new_article",
    )

    def test_add_package(self):
        package = TexPackage(name="testpkg")
        self.article.add_package(package)
        self.assertIn(package, self.article._packages)

    def test_add_text(self):
        text = "Additional text."
        self.article.add_text(text)
        self.assertIn(text, self.article._elements.values())

    def test_add_section(self):
        section_data = {"heading": "Test Section", "content": "Section content."}
        section = TexSection(**section_data)
        self.article.add_section(section)
        self.assertIn(section, self.article._elements.values())

    def test_add_textable(self):
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
        self.article.add_table(tex_table=table)
        self.assertIn(table.__str__(), self.article._elements.values())

    def test_add_paragraph(self):
        para = r"""Here is some paragraph. This I want to add into
my PlainArticle. But I don't know how?

Will You do that for me?
Please!
"""
        self.article.add_paragraph(para=para)
        self.assertIn("\n" + para + "\n", self.article._elements.values())


    def test_add_reference(self):
        ref = r"""@article{smith2020article,
  author = {Smith, John and Johnson, Jane},
  title = {An Example Article},
  journal = {Journal of Examples},
  year = {2020},
  volume = {10},
  pages = {1-10},
}
"""
        self.article.add_reference(reference=ref)
        self.assertIn(ref, self.article._references)


    def test_create_article(self):
        # Mock the creation process for testing purposes
        self.article.create = lambda: None
        # with self.assertWarns(DeprecationWarning):
        self.article.create()

    def test_show_output(self):
        # Mock the show output process for testing purposes
        self.article.show_output = lambda: None
        self.article.show_output()


if __name__ == '__main__':
    unittest.main()

