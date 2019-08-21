from Helper.Visual.Transform.Visual import Visual
from Helper.Load.classification import Classification
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates, andrews_curves
from sklearn.preprocessing import MinMaxScaler

class VClassification(Visual):
    def __init__(self, Transform, dir_ = "Data"):
        Visual.__init__(self, Transform, dir_)
        Visual.construct_figures(self)
        self.construct_figures()

    def construct_figures(self):
        print("In Classification-construct_figures")
        self.make_parallel_coordinates()
        self.make_andrews_curves()

    def make_parallel_coordinates(self):
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data)
        target = self.transform.load.partition.y_train.reset_index(drop=True)
        data = pd.concat([data, target], axis=1, sort=False)
        parallel_coordinates(data, *self.transform.load.outputs)
        plt.savefig(f"{self.dir_}/Visual/transform_parallel_coordinates.png",bbox_inches='tight')
        plt.close(fig)

    def make_andrews_curves(self):
        mm = MinMaxScaler()
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data)
        target = self.transform.load.partition.y_train.reset_index(drop=True)
        data = pd.concat([data, target], axis=1, sort=False)
        andrews_curves(data,*self.transform.load.outputs, colormap="Paired")
        plt.savefig(f"{self.dir_}/Visual/transform_andrews_curves.png", bbox_inches='tight')
        plt.close(fig)
