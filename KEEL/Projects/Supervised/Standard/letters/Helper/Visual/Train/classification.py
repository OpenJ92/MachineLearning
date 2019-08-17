from Helper.Train.Train import Train
from sklearn.metrics import confusion_matrix, classification_report
from Helper.Visual.Train.construct_confusion_matrix import annotate_heatmap, heatmap

import matplotlib.pyplot as plt
import numpy as np

class VClassification:
    def __init__(self, Train):
        self.train = Train
        self.load = self.train.load

    def construct_confusion_matrix(self):
        plt.rcParams["figure.figsize"] = (20,10)
        preds = self.train.clf.predict(self.load.partition.X_test)
        cm = confusion_matrix(self.load.partition.y_test.values, preds)
        class_ = np.unique(self.load.data[self.load.outputs].values)
        fig, ax = plt.subplots()
        im, cbar = heatmap(cm, class_, class_, ax, cmap="terrain", cbarlabel="Support")
        texts = annotate_heatmap(im, valfmt="{x:.1f} t")
        fig.tight_layout()
        plt.show()

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
        plt.show()
