from Helper.Load.load import Base_Load; import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


class Visual:
    def __init__(self, Load):
        self.load = Load
        self.mpl_config()

    def mpl_config(self):
        plt.rcParams["figure.figsize"] = (20,10)

    def construct_figures(self):
        print("In Visual-construct_figures")
        self.make_scatter_matrix()
        self.make_box()

    def make_box(self):
        fig, ax = plt.subplots()
        self.load.data[self.load.inputs].plot(kind='box', subplots=False, sharex=True, sharey=True)
        plt.savefig(f"Data/Visual/make_box.png", bbox_inches='tight')
        plt.close(fig)

    def make_scatter_matrix(self):
        fig, ax = plt.subplots()
        scatter_matrix(self.load.data[self.load.inputs], diagonal='kde')
        plt.savefig(f"Data/Visual/scatter_matrix.png", bbox_inches='tight')
        plt.close(fig)


