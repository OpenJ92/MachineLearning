from Helper.Visual.Visual import Visual
from Helper.Load.classification import Classification
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates, andrews_curves

class VClassification(Visual):
    def __init__(self, Transform):
        Visual.__init__(self, Transform)
        Visual.construct_figures(self)
        self.construct_figures()

    def construct_figures(self):
        print("In Classification-construct_figures")
        self.make_parallel_coordinates()
        self.make_andrews_curves()

    def make_parallel_coordinates(self):
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data, columns=self.transform.load.inputs)
        parallel_coordinates(data, *self.load.outputs)
        plt.savefig(f"Data/Visual/{self.transform}_parallel_coordinates.png",bbox_inches='tight')
        plt.close(fig)

    def make_andrews_curves(self):
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data, columns=self.transform.load.inputs)
        andrews_curves(data,*self.load.outputs, colormap="Paired")
        plt.savefig(f"Data/Visual/{self.transform}_andrews_curves.png", bbox_inches='tight')
        plt.close(fig)
