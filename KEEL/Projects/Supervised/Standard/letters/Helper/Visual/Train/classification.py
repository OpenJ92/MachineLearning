from sklearn.metrics import confusion_matrix, classification_report
from Helper.Visual.Train.construct_confusion_matrix import annotate_heatmap, heatmap

import matplotlib.pyplot as plt
import numpy as np

class VClassification:
    def __init__(self, Train, dir_ = "Data"):
        self.train = Train
        self.dir_ = dir_
        self.load = self.train.load
        self.construct_figures()

    def construct_figures(self):
        plt.rcParams["figure.figsize"] = (20,10)
        self.construct_confusion_matrix()
        self.construct_classification_report()

    def construct_confusion_matrix(self):
        preds = self.train.clf.predict(self.load.partition.X_test)
        cm = confusion_matrix(self.load.partition.y_test.values, preds)
        class_ = np.unique(self.load.data[self.load.outputs].values)
        fig, ax = plt.subplots()
        im, cbar = heatmap(cm, class_, class_, ax, cmap="terrain", cbarlabel="Support")
        texts = annotate_heatmap(im, valfmt="{x:.1f} t")
        fig.tight_layout()
        plt.savefig(f"{self.dir_}/Visual/train_confusion_matrix.png", bbox_inches='tight')

    def construct_classification_report(self):
        preds = self.train.clf.predict(self.load.partition.X_test)
        A = classification_report(self.load.partition.y_test.values, preds).split('\n')
        B = np.array([row.split() for row in A[3:-5]])
        A_ = A[0].split()
        C, D = B[:,0], B[:,1:-1].astype(float)
        fig, ax = plt.subplots()
        im, cbar = heatmap(D, C, A_, cmap="terrain")
        texts = annotate_heatmap(im, valfmt="{x:.1f} t")
        fig.tight_layout()
        plt.savefig(f"{self.dir_}/Visual/train_class_report.png", bbox_inches='tight')
