from Load.load import Base_Load
import matplotlib.pyplot as plt

class Visual:
    def __init__(self, Load):
        assert(isinstance(Load, Base_Load))
        self.Load = Load
