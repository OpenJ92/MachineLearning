from Helper.Partition.Partition import Partition

class ClassImbalancePartition(Partition):
    def __init__(self, Load, test_percentage):
        Partition.__init__(self, Load, test_percentage)
