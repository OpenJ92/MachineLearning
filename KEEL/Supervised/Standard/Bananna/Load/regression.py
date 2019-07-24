from Load.supervised import Supervised

class Regression(Supervised):
    def __init__(self, dir_, datafile, headerfile):
        Supervised.__init__(self, dir_, datafile, headerfile)
        self.type = "m" if len(self.outputs) else "s"
