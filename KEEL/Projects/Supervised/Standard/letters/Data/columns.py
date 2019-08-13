from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.ColumnSelector import ColumnSelector 
from Helper.Transform.Selector.TypeSelector import TypeSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from Helper.Load.classification import Classification
loadC = Classification("Data", "letter.dat", "letters-name.txt")

from sklearn.preprocessing import StandardScaler
from Helper.Transform.Custom.nominal import _Identity

continuous_ = {}
outputs_ = {}
inputs_number = column_pipeline(loadC.inputs, ColumnSelector, StandardScaler, continuous_)
outputs = column_pipeline(*loadC.outputs, TextSelector, _Identity, outputs_)

Column_ = {
    "inputs_c":inputs_number,
    "output":outputs
}