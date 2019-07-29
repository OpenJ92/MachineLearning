from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, LabelBinarizer, OneHotEncoder
from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector

class Dichotomous:
    def __init__(self, name, abstraction, selector, bounds, func, params):
        self.name = name
        self.abstraction = abstraction
        self.selector = self.selector_dictionary()[selector]
        self.bounds = bounds

    def selector_dictionary(self):
        return {"Number":NumberSelector, "Text":TextSelector}

    def pipline(self):
        return Pipeline([(f'{self.name}_selector', self.selector(self.name)),
                         (f'{self.abstraction}_transform', Binarizer(*[]))])
