import re
from Helper.Load.load import Base_Load

class Supervised(Base_Load):
    def __init__(self, dir_, datafile, headerfile):
        Base_Load.__init__(self, dir_, datafile, headerfile)
        self.outputs = self.read_outputs()

    def read_outputs(self):
        pattern = r'\@outputs.*\n'
        text = open(self.header_file(), "r").read()
        pt = re.search(pattern, text)[0]
        pt = pt.replace("@outputs", "").replace("\n", "").split(' ')
        pt = [i.replace(" ", "").replace(",","") for i in pt]
        return pt[1:]
