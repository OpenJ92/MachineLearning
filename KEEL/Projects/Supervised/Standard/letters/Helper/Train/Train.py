import pandas as pd
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

from Helper.Load.load import *

class Train:
    def __init__(self, Load, Model, Transform, columns=None, global_=PCA, hyperparameters=None):
        self.model = Model
        self.load = Load
        self.hyperparameters = hyperparameters
        self.columns = columns
        self.global_ = global_
        self.transform = Transform(self.load, self.columns, self.global_)
        self.pipeline = self.construct_pipeline()
        self.pipeline_params = self.pipeline.get_params()

    def construct_pipeline(self):
        return Pipeline([(f"inputs_pipeline", self.transform.inputs_pipeline),
                         (f"global", self.transform.globals_pipeline),
                         (f"estimator", self.model())])

    def construct_GSCV(self):
        return GridSearchCV(self.pipeline, self.hyperparameters, cv=10)

    def fit_GSCV(self):
        X = self.load.partition.X_train
        y = self.load.partition.y_train.values.ravel()
        GridSearch = self.construct_GSCV()
        GridSearch.fit(X, y)
        GridSearch.refit
        self.clf = GridSearch
        return GridSearch
