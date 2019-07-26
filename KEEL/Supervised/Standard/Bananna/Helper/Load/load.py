import pandas as pd
import re

class Base_Load:
    def __init__(self, dir_, datafile, headerfile):
        self.dir = dir_
        self.datafile = datafile
        self.headerfile = headerfile
        self.inputs, self.attributes = self.read_inputs(), self.read_attributes()

    def data(self):
        return pd.read_csv(f"{self.dir}/{self.datafile}", sep='\s*,\s*', engine='python')

    def describe(self):
        return self.data().describe()

    def header_file(self):
        return f"{self.dir}/{self.headerfile}"

    # Look to fix attributes function. We have to accout for
    #   all possible configurations. The bounds of the data will 
    #   become increasingly important over the Visual, Transform
    #   and ML classes.
    def read_attributes(self):
        pattern = r'\@attribute.*\n'
        text = open(self.header_file(), "r").read()
        pt = re.findall(pattern, text)
        pt = [i.replace("@attributes", "").replace("\n", "").split(' ') for i in pt]
        return pt

    def read_inputs(self):
        pattern = r'\@inputs.*\n'
        text = open(self.header_file(), "r").read()
        pt = re.search(pattern, text)[0]
        pt = pt.replace("@inputs", "").replace("\n", "").split(' ')
        pt = [i.replace(" ", "").replace(",", "") for i in pt]
        return pt[1:]
