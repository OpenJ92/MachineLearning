import pandas as pd
from Helper.Load.supervised import Supervised

class Classification(Supervised):
    def __init__(self, dir_, datafile, headerfile):
        Supervised.__init__(self, dir_, datafile, headerfile)
        self.type = "m" if len(self.outputs) else "s"

    def class_balance(self):
        return self.data.groupby(self.outputs).size()

    def integrate_dummies(self):
        return pd.get_dummies(self.data[self.outputs].astype(str), drop_first=True)
