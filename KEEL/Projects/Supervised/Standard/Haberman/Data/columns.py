from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from Helper.Transform.Custom.nominal import _LabelBinarizer

from sklearn.preprocessing import KBinsDiscretizer

_Age = {"n_bins": 15, "encode": "ordinal", "strategy": "uniform"}
_Year = {"n_bins": 10, "encode": "ordinal", "strategy": "uniform"}
_Positive = {"n_bins": 5, "encode": "ordinal", "strategy": "uniform"}
_Survival = {}

Age = column_pipeline("Age", NumberSelector, KBinsDiscretizer, _Age)
Year = column_pipeline("Year", NumberSelector, KBinsDiscretizer, _Year)
Positive = column_pipeline("Positive", NumberSelector, KBinsDiscretizer, _Positive)
Survival = column_pipeline("Survival", TextSelector, _LabelBinarizer, _Survival)

Column_pipeline_Dictionary = {"Age":Age,"Year":Year,"Positive":Positive,"Survival":Survival}

