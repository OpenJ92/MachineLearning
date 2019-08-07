import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from Helper.Transform.Transform.classification import Classification_Transform
from Helper.Load.load import *

class Train:
    def __init__(self, Load, Model, Transform, columns=None, hyperparameters=None):
        self.model = Model
        self.load = Load
        self.hyperparameters = hyperparameters
        self.columns = columns
        self.transform = Transform(self.load)
        self.pipeline = self.construct_pipeline()
        self.pipeline_params = self.pipeline.get_params()

    def construct_pipeline(self):
        return Pipeline([(f"inputs_pipeline", self.transform.inputs_pipeline),
                         (f"estimator", self.model())])

    def construct_GSCV(self):
        return GridSearchCV(self.pipeline, self.hyperparameters, cv=10)

    def fit_GSCV(self, hyperparameters):
        X = self.load.partition.X_train
        y = self.load.partition.y_train.values.ravel()
        GridSearch = self.construct_GSCV(hyperparameters)
        GridSearch.fit(X, y)
        GridSearch.refit
        return GridSearch
