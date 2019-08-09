from sklearn.pipeline import Pipeline
from Helper.Transform.Transform.transform import Base_Transform

class Supervised_Transform(Base_Transform):
    def __init__(self, Load, columns):
        Base_Transform.__init__(self, Load, columns)
        self.outputs = self.load.outputs

    def make_output_piplines(self):
        pipelines = []
        for pipeline in self.outputs:
            pipelines.append(self.columns[pipeline]._pipline())
        return pipelines
