from Helper.Visual.Visual import Visual
from Helper.Load.regression import Regression
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates, andrews_curves

class VRegression(Visual):
    def __init__(self, Load):
        assert isinstance(Load, Regression)
        super().__init__(Load)
        self.construct_figures()

    def construct_figures(self):
        self.make_parallel_coordinates()
        self.make_andrews_curves(self.load.inputs)
        self.make_andrews_curves(self.load.outputs)

    def make_parallel_coordinates(self):
        fig, ax = plt.subplots()
        parallel_coordinates(self.load.data(), class_column=None)
        plt.savefig("Data/Visual/parallel_coordinates.png", bbox_inches='tight')
        plt.close(fig)

    def make_andrews_curves(self, puts):
        fig, ax = plt.subplots()
        andrews_curves(self.load.data()[puts], class_column=None)
        plt.savefig(f"Data/Visual/{puts}_andrews_curves.png", bbox_inches='tight')
        plt.close(fig)


