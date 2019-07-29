from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np

Column_pipeline_Dictionary = {}

_Sex = {"handle_unknown":"ignore"}
_Rings = {"caetgories": np.array(list(range(100))).reshape(1,-1)}

Sex = column_pipeline("Sex", TextSelector, OneHotEncoder, _Sex)
Length = column_pipeline("Length", NumberSelector, StandardScaler, {})
Diameter = column_pipeline("Diameter", NumberSelector, StandardScaler, {})
Height = column_pipeline("Height", NumberSelector, StandardScaler, {})
Whole_weight = column_pipeline("Whole_weight", NumberSelector, StandardScaler, {})
Shucked_weight = column_pipeline("Shucked_weight", NumberSelector, StandardScaler, {})
Viscera_weight = column_pipeline("Viscera_weight", NumberSelector, StandardScaler, {})
Shell_weight = column_pipeline("Shell_weight", NumberSelector, StandardScaler, {})
Rings = column_pipeline("Rings", NumberSelector, OneHotEncoder, _Rings)

Column_pipeline_Dictionary = {
                                 "Sex":Sex,
                                 "Length":Length, 
                                 "Diameter":Diameter,
                                 "Height":Height,
                                 "Whole_weight":Whole_weight,
                                 "Shucked_weight":Shucked_weight,
                                 "Viscera_weight":Viscera_weight,
                                 "Shell_weight":Shell_weight,
                                 "Rings": Rings
                              }
