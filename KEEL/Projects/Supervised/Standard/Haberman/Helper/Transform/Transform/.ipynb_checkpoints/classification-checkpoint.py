from Helper.Transform.Transform.supervised import  Supervised_Transform
from sklearn.pipeline import FeatureUnion, Pipeline

class Classificaton_Transform(Supervised_Transform):
    def __init__(self, Load):
        Supervised_Transform.__init__(self, Load)
        self.inputs_pipeline, self.outputs_pipeline = self.assemble_pipelines()
        self._fit()

    def _fit(self):
        self.inputs_pipeline.fit(self.load.partition.X_train)
        self.outputs_pipeline.fit(self.load.partition.y_train)

    def _transform(self, X, y):
        return self.inputs_pipeline.transform(X), self.outputs_pipeline.transform(y)

    def assemble_pipelines(self):
        inputs_pipeline = Pipeline([("inputs", FeatureUnion(list(zip(self.inputs, self.make_input_piplines()))))])
        outputs_pipeline = Pipeline([("outputs", FeatureUnion(list(zip(self.outputs, self.make_output_piplines()))))])
        return inputs_pipeline, outputs_pipeline
    
    def featureU(self):
        return FeatureUnion([("inputs_",self.inputs_pipeline),("outputs_",self.outputs_pipeline)])

