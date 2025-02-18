import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from Data.hyperparameters import hyperparameters

class Train:
    def __init__(self, Load, Transform, Model):
        self.model = Model
        self.load = Load
        self.transform = Transform(self.load)
        self.pipeline = self.construct_pipeline()
        self.pipeline_params = self.pipeline.get_params()

    def construct_pipeline(self):
        return Pipeline([(f"pipeline", self.transform.inputs_pipeline),
                         (f"estimator", self.model())])

    def construct_GSCV(self, hyperparameters):
        return GridSearchCV(self.pipeline, hyperparameters, cv=10)

    def fit_GSCV(self):
        X = self.load.partition.X_train
        y_values = self.transform.outputs_pipeline.transform(self.load.partition.y_train)
        y = pd.DataFrame(y_values)
