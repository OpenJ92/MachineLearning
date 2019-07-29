from sklearn.pipeline import Pipeline
from Helper.Transform.Columns.columns import Column_pipeline_Dictionary
from Helper.Transform.transform import Base_Transform

class Supervised_Transform(Base_Transform):
    def __init__(self, Load):
        Base_Transform.__init__(self, Load)
        self.outputs = self.load.outputs

    def make_output_piplines(self):
        pipelines = []
        for pipeline in self.outputs:
            pipelines.append(Column_pipeline_Dictionary[pipeline]._pipline())
        return pipelines
