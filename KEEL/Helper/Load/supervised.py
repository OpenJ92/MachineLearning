import re
from sklearn.model_selection import train_test_split
from Helper.Load.load import Base_Load

class Supervised(Base_Load):
    def __init__(self, dir_, datafile, headerfile):
        Base_Load.__init__(self, dir_, datafile, headerfile)
        self.outputs = self.read_outputs()
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data[self.inputs], self.data[self.outputs], test_size=.2, random_state=10)

    def read_outputs(self):
        pattern = r'\@outputs.*[\n]?'
        text = open(self.header_file(), "r").read()
        pt = re.search(pattern, text)[0]
        pt = pt.replace("@outputs", "").replace("\n", "").split(' ')
        pt = [i.replace(" ", "").replace(",","") for i in pt]
        return pt[1:]
