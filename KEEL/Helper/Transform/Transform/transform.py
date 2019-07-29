from sklearn.pipeline import Pipeline
from Helper.Transform.Columns.columns import Column_pipeline_Dictionary

class Base_Transform:
    def __init__(self, Load):
        self.load = Load 
        self.inputs = self.load.inputs

    def make_input_piplines(self):
        pipelines = []
        for pipeline in self.inputs:
            pipelines.append(Column_pipeline_Dictionary[pipeline]._pipline())
        return pipelines
