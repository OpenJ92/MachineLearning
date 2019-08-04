from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from Helper.Transform.Custom.nominal import _LabelBinarizer

_Led1 = {}
_Led2 = {}
_Led3 = {}
_Led4 = {}
_Led5 = {}
_Led6 = {}
_Led7 = {}
_number = {}

Led1 = column_pipeline("Led1", NumberSelector, _LabelBinarizer, _Led1)
Led2 = column_pipeline("Led2", NumberSelector, _LabelBinarizer, _Led2)
Led3 = column_pipeline("Led3", NumberSelector, _LabelBinarizer, _Led3)
Led4 = column_pipeline("Led4", NumberSelector, _LabelBinarizer, _Led4)
Led5 = column_pipeline("Led5", NumberSelector, _LabelBinarizer, _Led5)
Led6 = column_pipeline("Led6", NumberSelector, _LabelBinarizer, _Led6)
Led7 = column_pipeline("Led7", NumberSelector, _LabelBinarizer, _Led7)
number = column_pipeline("Number", NumberSelector, _LabelBinarizer, _number)

Column_pipeline_Dictionary = {
        "Led1":Led1,
        "Led2":Led2,
        "Led3":Led3,
        "Led4":Led4,
        "Led5":Led5,
        "Led6":Led6,
        "Led7":Led7,
        "Number":number
        }
