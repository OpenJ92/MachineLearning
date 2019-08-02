class Train:
    def __init__(self, Load, Transform, Model):
        self.model = Model
        self.load = Load
        self.transform = Transform(self.load)
