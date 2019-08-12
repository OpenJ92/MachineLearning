from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from sklearn.preprocessing import StandardScaler, OneHotEncoder

At1 = column_pipeline("At1", NumberSelector, StandardScaler, {})
At2 = column_pipeline("At2", NumberSelector, StandardScaler, {})
Class = column_pipeline("Class", NumberSelector, OneHotEncoder, {"categories":"auto"})

Column_pipeline_Dictionary = {"At1":At1, "At2":At2, "Class":Class}
