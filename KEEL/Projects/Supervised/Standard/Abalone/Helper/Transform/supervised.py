from sklearn.pipeline import Pipeline
from Helper.Transform.transform import Base_Transform

class Supervised_Transform(Base_Transform):
    def __init__(self, Load):
        Base_Transform.__init__(self, Load)
        self.outputs = self.load.outputs

    def make_output_piplines(self):
        piplines = []
        for column in self.outputs:
            column_dict = self.attributes[column]
            A = self.abstraction_dictionary()[column_dict["abstraction"]](**column_dict)
            piplines.append(A.pipline)
        return piplines
