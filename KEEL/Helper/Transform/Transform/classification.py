from Helper.Transform.supervised import  Supervised_Transform
from sklearn.pipeline import FeatureUnion, Pipeline

class Classificaton_Transform(Supervised_Transform):
    def __init__(self, Load):
        Supervised_Transform.__init__(self, Load)

    def assemble_pipelines(self):
        return Pipeline([("feats", FeatureUnion(list(zip(self.inputs, self.make_input_piplines()))))])

    def train_pipline(self):
        pass
