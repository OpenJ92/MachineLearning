from Load.supervised import Supervised

class Regression(Supervised):
    def __init__(self, dir_, datafile, headerfile):
        super().__init__(self, dir_, datafile, headerfile)
