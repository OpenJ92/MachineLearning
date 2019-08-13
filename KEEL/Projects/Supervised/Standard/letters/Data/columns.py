from Helper.Transform.Selector.NumberSelector import NumberSelector
from Helper.Transform.Selector.TextSelector import TextSelector
from Helper.Transform.Columns.column_pipeline import column_pipeline

from sklearn.preprocessing import StandardScaler
from Helper.Transform.Custom.nominal import _Identity

X_box_ = {}
Y_box_ = {}
Width_ = {}
High_ = {}
Onpix_ = {}
X_bar_ = {}
Y_bar_ = {}
X2bar_ = {}
Y2bar_ = {}
Xybar_ = {}
X2ybr_ = {}
Xy2br_ = {}
X_ege_ = {}
Xegvy_ = {}
Y_ege_ = {}
Yegvx_ = {}
Class_ = {}

X_box = column_pipeline("X-box", NumberSelector, StandardScaler, X_box_)
Y_box = column_pipeline("Y-box", NumberSelector, StandardScaler, Y_box_)
Width = column_pipeline("Width", NumberSelector, StandardScaler, Width_)
High = column_pipeline("High", NumberSelector, StandardScaler, High_)
Onpix = column_pipeline("Onpix", NumberSelector, StandardScaler, Onpix_)
X_bar = column_pipeline("X-bar", NumberSelector, StandardScaler, X_bar_)
Y_bar = column_pipeline("Y-bar", NumberSelector, StandardScaler, Y_bar_)
X2bar = column_pipeline("X2bar", NumberSelector, StandardScaler, X2bar_)
Y2bar = column_pipeline("Y2bar", NumberSelector, StandardScaler, Y2bar_)
Xybar =column_pipeline("Xybar", NumberSelector, StandardScaler, Xybar_)
X2ybr = column_pipeline("X2ybr", NumberSelector, StandardScaler, X2ybr_)
Xy2br = column_pipeline("Xy2br", NumberSelector, StandardScaler, X2ybr_)
X_ege = column_pipeline("X-ege", NumberSelector, StandardScaler, X_ege_)
Xegvy = column_pipeline("Xegvy", NumberSelector, StandardScaler, Xegvy_)
Y_ege = column_pipeline("Y-ege", NumberSelector, StandardScaler, Y_ege_)
Yegvx = column_pipeline("Yegvx", NumberSelector, StandardScaler, Yegvx_)
Class = column_pipeline("Class", TextSelector, _Identity, Class_)

Column_pipeline_Dictionary = {
        "X-box":X_box,
        "Y-box":Y_box,
        "Width":Width,
        "High":High,
        "Onpix":Onpix,
        "X-bar":X_bar,
        "Y-bar":Y_bar,
        "X2bar":X2bar,
        "Y2bar":Y2bar,
        "Xybar":Xybar,
        "X2ybr":X2ybr,
        "Xy2br":Xy2br,
        "X-ege":X_ege,
        "Xegvy":Xegvy,
        "Y-ege":Y_ege,
        "Yegvx":Yegvx,
        "Class":Class
        }
