class TreeNode:
    def __init__(self, value, parent=None, distance=0, action='Start at'):
        self.value = value
        self.parent = parent
        self.distance = distance
        self.action = f"{action} {value}" if parent is None else f"from {parent.value}, {action} {value}"

        self.children = []

    def add_child(self, value, distance=0, action="go to"):
        self.children.append(TreeNode(value, self, distance, action))

    def add_child_node(self, child_node):
        self.children.append(child_node)

    def get_distance_from_root(self):
        distance = self.distance
        aux = self.parent
        while aux:
            distance += aux.distance
            aux = aux.parent
        return distance

    def get_ancestors(self):
        aux = self.parent
        ancestors = []

        while aux:
            ancestors.append(aux.value)
            aux = aux.parent
        return ancestors

    def print(self, strategy="BFS"):
        explored_values = []
        frontier_values = []
        frontier = [self]
        while len(frontier) > 0:
            if strategy == "BFS":
                curr_element = frontier.pop(0)
            if strategy == "DFS":
                curr_element = frontier.pop()
            explored_values.append(curr_element.value)
            new_frontier = [child for child in curr_element.children if
                            child.value not in explored_values and child.value not in frontier_values]
            frontier.extend(new_frontier)
            frontier_values.extend([node.value for node in new_frontier])

            line = str(curr_element.value) + ": "

            child_values = [str(child.value) for child in curr_element.children]
            line += '\t'.join(child_values)
            print(line)
