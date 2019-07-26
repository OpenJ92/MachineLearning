from Helper.Load.load import Base_Load; import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix, parallel_coordinates, andrews_curves


class Visual:
    def __init__(self, Load):
        self.load = Load
        self.construct_figures()

    def construct_figures(self):
        plt.rcParams["figure.figsize"] = (20,10)
        self.make_parallel_coordinates()
        self.make_andrews_curves()
        self.make_scatter_matrix()
        self.make_box()

    def make_box(self):
        fig, ax = plt.subplots()
        self.load.data()[self.load.inputs].plot(kind='box', subplots=False, sharex=True, sharey=True)
        plt.savefig("Data/Visual/box.png", bbox_inches='tight')
        plt.close(fig)

    def make_scatter_matrix(self):
        fig, ax = plt.subplots()
        scatter_matrix(self.load.data()[self.load.inputs], diagonal='kde')
        plt.savefig("Data/Visual/scatter_matrix.png", bbox_inches='tight')
        plt.close(fig)

    def make_parallel_coordinates(self):
        fig, ax = plt.subplots()
        parallel_coordinates(self.load.data(), *self.load.outputs)
        plt.savefig("Data/Visual/parallel_coordinates.png", bbox_inches='tight')
        plt.close(fig)

    def make_andrews_curves(self):
        fig, ax = plt.subplots()
        andrews_curves(self.load.data(),*self.load.outputs)
        plt.savefig("Data/Visual/andrews_curves.png", bbox_inches='tight')
        plt.close(fig)
