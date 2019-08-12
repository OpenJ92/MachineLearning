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
