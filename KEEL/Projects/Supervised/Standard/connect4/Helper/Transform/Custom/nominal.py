from sklearn.preprocessing import LabelBinarizer

from sklearn.base import TransformerMixin 

class _Identity(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = None 

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return X


class _LabelBinarizer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        self.encoder = LabelBinarizer(*args, **kwargs)

    def fit(self, X, y=None):
        self.encoder.fit(X)
        return self

    def transform(self, X, y=None):
        return self.encoder.transform(X)

#this class is not functioning properly currently. There's a problem 
#with our capability to inject this as a global transform to the data
#X. Take another look at this when you have the opportunity.
class _Arithmetic_Transformer(TransformerMixin):
    def __init__(self, *args, **kwargs):
        if kwargs["func"] == None:
            kwargs["func"] = lambda X: X
        self.encoder = kwargs['func']
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return self.func(X)
