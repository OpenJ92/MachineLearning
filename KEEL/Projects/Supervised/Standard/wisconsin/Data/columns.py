from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from Helper.Transform.Custom.nominal import _Identity

_ClumpThickness = {}
_CellSize = {}
_CellShape = {}
_MaginalAdhesion = {}
_EpithelialSize = {}
_BareNuclei = {}
_BlandChromatin = {}
_NormalNucleoli = {}
_Mitoses = {}
_Class = {}

ClumpThickness = column_pipeline("ClumpThickness", NumberSelector, _Identity, _ClumpThickness)
CellSize = column_pipeline("CellSize", NumberSelector, _Identity,_CellSize)
CellShape = column_pipeline("CellShape", NumberSelector, _Identity,_CellShape)
MaginalAdhesion = column_pipeline("MarginalAdhesion", NumberSelector, _Identity,_MaginalAdhesion)
EpithelialSize = column_pipeline("EpithelialSize", NumberSelector, _Identity, _EpithelialSize)
BareNuclei = column_pipeline("BareNuclei", NumberSelector, _Identity,_BareNuclei )
BlandChromatin = column_pipeline("BlandChromatin", NumberSelector, _Identity,_BlandChromatin)
NormalNucleoli = column_pipeline("NormalNucleoli", NumberSelector, _Identity,_NormalNucleoli)
Mitoses = column_pipeline("Mitoses", NumberSelector, _Identity,_Mitoses)
Class = column_pipeline("Class", NumberSelector, _Identity,_Class)

Column_pipeline_Dictionary = {
            "ClumpThickness" : ClumpThickness,
            "CellSize" : CellSize,
            "CellShape" : CellShape,
            "MarginalAdhesion" : MaginalAdhesion,
            "EpithelialSize" : EpithelialSize,
            "BareNuclei" : BareNuclei,
            "BlandChromatin" : BlandChromatin,
            "NormalNucleoli" : NormalNucleoli,
            "Mitoses" : Mitoses,
            "Class" : Class
                            }

