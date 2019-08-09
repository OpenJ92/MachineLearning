from Helper.Transform.Transform.supervised import  Supervised_Transform
from sklearn.pipeline import FeatureUnion, Pipeline
import pandas as pd

class Classificaton_Transform(Supervised_Transform):
    def __init__(self, Load, columns, global_):
        Supervised_Transform.__init__(self, Load, columns, global_)
        self.load = Load
        self.class_balance = self.load.class_balance
        self.inputs_pipeline, self.outputs_pipeline, self.globals_pipeline  = self.assemble_pipelines()
        self._fit()
        self.data = self.globals_pipeline.transform(self.inputs_pipeline.transform(self.load.partition.X_train))

    def _fit(self):
        self.inputs_pipeline.fit(self.load.partition.X_train)
        self.outputs_pipeline.fit(self.load.partition.y_train)
        self.globals_pipeline.fit(self.inputs_pipeline.transform(self.load.partition.X_train))

    def _transform(self, X, y):
        return self.inputs_pipeline.transform(X), self.outputs_pipeline.transform(y)

    def assemble_pipelines(self):
        inputs_pipeline = Pipeline([("inputs", FeatureUnion(list(zip(self.inputs, self.make_input_piplines()))))])
        outputs_pipeline = Pipeline([("outputs", FeatureUnion(list(zip(self.outputs, self.make_output_piplines()))))])
        globals_pipeline = Pipeline([("globals", self.make_global_pipelines())])
        return inputs_pipeline, outputs_pipeline, globals_pipeline
