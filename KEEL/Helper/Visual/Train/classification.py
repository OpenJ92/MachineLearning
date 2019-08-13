from Helper.Train.Train import Train
from sklearn.metrics import confusion_matrix, classification_report

class VClassification:
    def __init__(self, Train):
        self.train = Train
        self.load = self.train.load

    def construct_confuation_matrix(self):
        preds = self.train.clf.predict(self.load.partition.X_test)
        cm = confusion_matrix(self.load.partition.y_test.values, preds)
