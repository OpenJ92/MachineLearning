from Helper.Transform.supervised import  Supervised_Transform
from Helper.Transform.DataAbstraction.Continuous import Continuous
from Helper.Transform.DataAbstraction.Dichotomous import Dichotomous
from Helper.Transform.DataAbstraction.Nominal import Nominal
from Helper.Transform.DataAbstraction.Ordinal import Ordinal

class Classificaton_Transform(Supervised_Transform):
    def __init__(self, Load):
        Supervised_Transform.__init__(self, Load)

    def assemble_pipelines(self):
        pass

    def train_pipline(self):
        pass
