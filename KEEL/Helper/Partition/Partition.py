from sklearn.model_selection import train_test_split

class Partition:
    def __init__(self, Load, test_percentage):
        self.load = Load
        self.test_percentage = test_percentage
        self.train_percentage = 1 - test_percentage
        self.X_train, self.X_test, self.y_train, self.y_test = self.make_partition()

    def make_partition(self):
        return train_test_split(self.load.data[self.load.inputs],
                                self.load.data[self.load.outputs],
                                test_size=self.test_percentage,
                                random_state=42)
