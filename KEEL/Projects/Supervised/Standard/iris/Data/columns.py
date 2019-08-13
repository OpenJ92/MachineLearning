from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from sklearn.preprocessing import StandardScaler
from Helper.Transform.Custom.nominal import _Identity

SepalLength_ = {}
SepalWidth_ = {}
PetalLength_ = {}
PetalWidth_ = {}
Class_ = {}

SepalLength = column_pipeline("SepalLength", NumberSelector, StandardScaler, SepalLength_)
SepalWidth = column_pipeline("SepalWidth", NumberSelector, StandardScaler, SepalWidth_)
PetalLength = column_pipeline("PetalLength", NumberSelector, StandardScaler, PetalLength_)
PetalWidth = column_pipeline("PetalWidth", NumberSelector, StandardScaler, PetalWidth_)
Class =  column_pipeline("Class", NumberSelector, _Identity, Class_)

Column_pipeline_Dictionary = {
    "SepalLength": SepalLength,
    "SepalWidth": SepalWidth,
    "PetalLength": PetalLength,
    "PetalWidth": PetalWidth,
    "Class": Class
}
