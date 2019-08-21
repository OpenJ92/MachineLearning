from sklearn.pipeline import Pipeline

class Base_Transform:
    def __init__(self, Load, columns, global_):
        self.load = Load
        self.inputs = self.load.inputs
        self.columns = columns
        self.global_ = global_

        
    def make_input_piplines(self):
        pipelines = []
        for name, pipeline in self.columns.items():
            if "input" in name:
                pipelines.append(pipeline._pipline())
        return pipelines

    def make_global_pipelines(self):
        return self.global_()
