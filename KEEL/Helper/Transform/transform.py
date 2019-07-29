from sklearn.pipeline import Pipeline
from Helper.Transform.DataAbstraction.Continuous import Continuous
from Helper.Transform.DataAbstraction.Dichotomous import Dichotomous
from Helper.Transform.DataAbstraction.Nominal import Nominal
from Helper.Transform.DataAbstraction.Ordinal import Ordinal

class Base_Transform:
    def __init__(self, Load):
        self.load = Load
        self.attributes = self.load.read_transform_config()["attribute"] 
        self.inputs = self.load.inputs

    def abstraction_dictionary(self):
        return {"Continuous":Continuous, "Dichotomous":Dichotomous, "Nominal":Nominal, "Ordinal":Ordinal}

    def make_input_piplines(self):
        piplines = []
        for column in self.inputs:
            column_dict = self.attributes[column]
            print(column_dict)
            A = self.abstraction_dictionary()[column_dict["abstraction"]](**column_dict)
            piplines.append(A.pipline())
        return piplines
