from sklearn.pipeline import Pipeline

class column_pipeline:
    def __init__(self, col, selector, func, params):
        self.col = col
        self.selector = selector
        self.func = func
        self.params = params

    def _pipline(self):
        return Pipeline([(f'{self.col}_selector', self.selector(self.col)),
                         (f'{self.func.__name__}_transform', self.func(**self.params))])
