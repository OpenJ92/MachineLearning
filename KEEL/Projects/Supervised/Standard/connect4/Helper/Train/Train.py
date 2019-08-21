import pandas as pd
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from joblib import dump, load
import os

from Helper.Visual.Load.classification import VClassification as loadVC
from Helper.Visual.Transform.classification import VClassification as transformVC
from Helper.Visual.Train.classification import VClassification as trainVC

class Train:
    def __init__(self, Load, Model, Transform, hyperparameters=None):
        self.model = Model
        self.load = Load
        self.transform = Transform
        self.hyperparameters = hyperparameters
        self.pipeline = self.construct_pipeline()
        self.pipeline_params = self.pipeline.get_params()

    def construct_pipeline(self):
        return Pipeline([(f"inputs", self.transform.inputs_pipeline),
                         (f"global", self.transform.globals_pipeline),
                         (f"estimator", self.model)])

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

    def make_experiment(self, name):
        assert(self.clf != None)
        dir_ = os.getcwd() + "/Experiments/" + name
        os.mkdir(dir_)
        os.mkdir(dir_ + "/Visual")
        os.mkdir(dir_ + "/Model")
        os.mkdir(dir_ + "/Markdown")
        os.mkdir(dir_ + "/Data")

        #loadVC(self.load, dir_)
        transformVC(self.transform, dir_)
        trainVC(self, dir_)

        dump(self.clf, f"{dir_}/Model/{name}.joblib")
        dump(self, f"{dir_}/Model/train.joblib")
        dump(self.load, f"{dir_}/Model/load.joblib")

        os.rename("columns.py", f"Experiments/{name}/Data/columns.py")
        os.rename("hyperparameters.py", 
                 f"Experiments/{name}/Data/hyperparameters.py")
        
        
