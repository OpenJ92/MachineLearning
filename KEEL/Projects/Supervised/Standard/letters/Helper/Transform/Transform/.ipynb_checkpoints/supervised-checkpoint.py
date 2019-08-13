from sklearn.pipeline import Pipeline
from Helper.Transform.Transform.transform import Base_Transform

class Supervised_Transform(Base_Transform):
    def __init__(self, Load, columns, global_):
        Base_Transform.__init__(self, Load, columns, global_)
        self.columns = columns
        self.outputs = self.load.outputs

    def make_output_piplines(self):
        pipelines = []
        for name, pipeline in self.columns.items():
            if "output" in name:
                pipelines.append(pipeline._pipline())
        return pipelines
