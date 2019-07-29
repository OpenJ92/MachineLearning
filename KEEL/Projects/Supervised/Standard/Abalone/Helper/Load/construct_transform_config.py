import re
import json

class construct_transform_config:
    def __init__(self, dir_, datafile, headerfile):
        self.dir = dir_
        self.datafile = datafile
        self.headerfile = headerfile
        self.push_to_file()

    def push_to_file(self):
        json_ = self.construct_json()
        with open("Data/transform_config.json", "w") as outfile:
            json.dump(json_, outfile)

    def construct_json(self):
        dict_ = {"attribute":{}, "inputs":[], "outputs":[]}
        for attribute in self.read_attributes():
            dict_['attribute'][attribute[1]] = {"name":attribute[1], "abstraction":None, "selector":None, "bounds":None, "func":None, "params":None}
        dict_["inputs"] = self.read_inputs()
        dict_["outputs"] = self.read_outputs()
        return dict_

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

    def read_outputs(self):
        pattern = r'\@outputs.*[\n]?'
        text = open(self.header_file(), "r").read()
        pt = re.search(pattern, text)[0]
        pt = pt.replace("@outputs", "").replace("\n", "").split(' ')
        pt = [i.replace(" ", "").replace(",","") for i in pt]
        return pt[1:]
