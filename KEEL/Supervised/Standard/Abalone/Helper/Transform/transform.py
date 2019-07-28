from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector

class Base_Transform:
    def __init__(self, Load):
        self.load = Load
        self.attributes = self.load.attributes
        self.inputs = self.load.inputs

    def selector_dictionary(self):
        return {"Number":NumberSelector, "Text":TextSelector}

    def make_input_piplines(self):
        pass
