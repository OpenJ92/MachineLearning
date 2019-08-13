from Helper.Transform.Transform.transform import Base_Transform

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

class Visual:
    def __init__(self, Transform):
       self.transform = Transform
       self.mpl_config()

    def mpl_config(self):
        plt.rcParams["figure.figsize"] = (20,10)

    def construct_figures(self):
        print("In Visual-construct_figures")
        self.make_scatter_matrix()
        self.make_box()

    def make_box(self):
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data)
        data.plot(kind='box', subplots=False, sharex=True, sharey=True)
        plt.savefig(f"Data/Visual/{self.transform}_make_box.png", bbox_inches='tight')
        plt.close(fig)

    def make_scatter_matrix(self):
        fig, ax = plt.subplots()
        data = pd.DataFrame(self.transform.data)
        scatter_matrix(data, diagonal='kde')
        plt.savefig(f"Data/Visual/{self.transform}_scatter_matrix.png", bbox_inches='tight')
        plt.close(fig)


