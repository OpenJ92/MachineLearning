from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.transform import Base_Transform

class Supervised_Transform(Base_Transform):
    def __init__(self, Load):
        Base_Transform.__init__(self, Load)
        self.outputs = self.load.outputs

    def make_output_piplines(self):
        pass
