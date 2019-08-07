from sklearn.pipeline import Pipeline

class Base_Transform:
    def __init__(self, Load, columns):
        self.load = Load 
        self.inputs = self.load.inputs
        self.columns = columns

    def make_input_piplines(self):
        pipelines = []
        for pipeline in self.inputs:
            pipelines.append(self.columns[pipeline]._pipline())
        return pipelines

    def make_global_input_pipeline(self):
        pass
