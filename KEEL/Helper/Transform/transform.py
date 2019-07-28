from sklearn.pipeline import Pipeline
from Helper.Transform.DataAbstraction.Continuous import Continuous
from Helper.Transform.DataAbstraction.Dichotomous import Dichotomous
from Helper.Transform.DataAbstraction.Nominal import Nominal
from Helper.Transform.DataAbstraction.Ordinal import Ordinal

class Base_Transform:
    def __init__(self, Load):
        self.load = Load
        self.attributes = self.load.attribute_dictionary()
        self.inputs = self.load.inputs

    def selector_dictionary(self):
        return {"Number":NumberSelector, "Text":TextSelector}

    def make_input_piplines(self):
        pass
