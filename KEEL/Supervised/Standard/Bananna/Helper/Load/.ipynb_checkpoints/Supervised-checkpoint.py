from Load import Load
import re

class Supervised(Load):
    def __init__(self, dir_, datafile, headerfile):
        super().__init__(dir_, datafile, headerfile)
        self.inputs, self.outputs = self.load()

    def read_names(self, type_="inputs"):
        pattern = r"@{type_}?\/n"
        text = open(self.header_file, "r").read()
        import pdb;pdb.set_trace()

    def load(self):
        return 0,0
