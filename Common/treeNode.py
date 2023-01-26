class TreeNode:
    def __init__(self, value, parent=None, distance=0):
        self.value = value
        self.parent = parent
        self.distance = distance
        self.children = []

    def add_child(self, value, distance=0):
        self.children.append(TreeNode(value, self, distance))

    def get_distance_from_root(self):
        distance = self.distance
        aux = self.parent
        while aux is not None:
            distance += aux.distance
            aux = aux.parent
        return distance
