from Helper.Train.Train import Train
from sklearn.metrics import confusion_matrix, classification_report
from Helper.Visual.Train.construct_confusion_matrix import annotate_heatmap, heatmap

import matplotlib.pyplot as plt
import numpy as np

class VClassification:
    def __init__(self, Train):
        self.train = Train
        self.load = self.train.load

    def construct_confuation_matrix(self):
        plt.rcParams["figure.figsize"] = (20,10)
        preds = self.train.clf.predict(self.load.partition.X_test)
        cm = confusion_matrix(self.load.partition.y_test.values, preds)
        class_ = np.unique(self.load.data[self.load.outputs].values)
        fig, ax = plt.subplots()
        im, cbar = heatmap(cm, class_, class_, ax, cmap="terrain", cbarlabel="Support")
        texts = annotate_heatmap(im, valfmt="{x:.1f} t")
        fig.tight_layout()
        plt.show()
