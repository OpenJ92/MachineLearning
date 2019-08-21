from Helper.Visual.Load.Visual import Visual
from Helper.Load.classification import Classification
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates, andrews_curves

class VClassification(Visual):
    def __init__(self, Load, dir_ = "Data"):
        Visual.__init__(self, Load, dir_)
        Visual.construct_figures(self)
        self.construct_figures()

    def construct_figures(self):
        print("In Classification-construct_figures")
        self.make_parallel_coordinates()
        self.make_andrews_curves()
        self.make_class_balance()

    def make_parallel_coordinates(self):
        fig, ax = plt.subplots()
        parallel_coordinates(self.load.data, *self.load.outputs)
        plt.savefig(f"{self.dir_}/Visual/load_parallel_coordinates.png", bbox_inches='tight')
        plt.close(fig)

    def make_andrews_curves(self):
        fig, ax = plt.subplots()
        andrews_curves(self.load.data,*self.load.outputs, colormap="Paired")
        plt.savefig(f"{self.dir_}/Visual/load_andrews_curves.png", bbox_inches='tight')
        plt.close(fig)

    def make_class_balance(self):
        fig, ax = plt.subplots()
        self.load.class_balance().plot(kind='bar', subplots=False, sharex=True, sharey=True)
        plt.savefig(f"{self.dir_}/Visual/load_class_balance.png", bbox_inches='tight')
        plt.close(fig)




