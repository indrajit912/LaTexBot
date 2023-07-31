# Tests will be performed here.
# Author: Indrajit Ghosh
# Created On: Jul 30, 2023

from latex import *

class LatexTable:
    def __init__(self, columns):
        self.columns = columns
        self.rows = []
        self.longtable = False

    def add_row(self, values):
        self.rows.append(values)

    def enable_longtable(self):
        self.longtable = True

    def _generate_table_code(self):
        col_spec = '|'.join(['c'] * len(self.columns))
        table_code = f"\\begin{{longtable}}{{{col_spec}}}\\hline\n" if self.longtable else "\\begin{tabular}{|c|}\n"
        table_code += " & ".join(self.columns) + " \\\\\\hline\hline\n"
        
        for row in self.rows:
            table_code += " & ".join(str(val) for val in row) + " \\\\\n"

        table_code += f"\\end{{longtable}}\n" if self.longtable else "\\end{tabular}\n"

        return table_code

    def to_latex(self):
        latex_code = self._generate_table_code()
        return latex_code



def main():

    # Example Usage:

    table = LatexTable(["Name", "Age", "Occupation"])
    
    table.add_row(["John Doe", 30, "Engineer"])
    table.add_row(["Jane Smith", 28, "Scientist"])
    table.add_row(["Michael Johnson", 35, "Teacher"])
    
    table.enable_longtable()
    
    latex_code = table.to_latex()
    print(latex_code)
    

if __name__ == '__main__':
    main()
    