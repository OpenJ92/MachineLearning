import pandas as pd

class Load:
    def __init__(self, dir_, datafile, headerfile):
        self.dir = dir_
        self.datafile = datafile
        self.headerfile = headerfile

    def data(self):
        return pd.read_csv(f"{self.dir}/{self.datafile}")
