import pandas as pd
import numpy as np
import json
import re

class Base_Load:
    def __init__(self, dir_, datafile, headerfile):
        self.dir = dir_
        self.datafile = datafile
        self.headerfile = headerfile
        self.inputs, self.attributes = self.read_inputs(), self.read_attributes()
        self.data, self.data_with_null = self.construct_data()

    def _data(self):
        df = pd.read_csv(f"{self.dir}/{self.datafile}",
                         sep='\s*,\s*',
                         engine='python',
                         na_values="<null>")
        not_null = df.isnull().any(axis=1)
        return df[~not_null], df[not_null]

    def describe(self):
        return self.data.describe()

    def header_file(self):
        return f"{self.dir}/{self.headerfile}"

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

    def attribute_dictionary(self):
        dictionary = []
        for attribute in self.attributes:
            dictionary.append({"name":attribute[1], "type": attribute[2], "bounds":attribute[3]})
        return dictionary

    def construct_data(self):
        return self._data()

