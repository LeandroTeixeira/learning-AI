from Common.treeNode import TreeNode


class Graph:
    def __init__(self, vertices: list):
        self.graph = dict()
        for vertice in vertices:
            self.graph[vertice] = dict()
            for aux_vertice in vertices:
                self.graph[vertice][aux_vertice] = 0

    def add_connection(self, src, target, value=1, directed=False):
        if src not in self.graph.keys():
            self.graph[src] = dict()
            for key in self.graph.keys():
                self.graph[src][key] = 0
                self.graph[key][src] = 0

        if target not in self.graph.keys():
            self.graph[target] = dict()
            for key in self.graph.keys():
                self.graph[target][key] = 0
                self.graph[key][target] = 0

        self.graph[src][target] = value
        if directed is False:
            self.graph[target][src] = value

        return self.graph

    def remove_connection(self, src, target, directed=False):
        self.graph[src][target] = 0
        if directed is False:
            self.graph[target][src] = 0
        return self.graph

    def to_graph(self, node=None):

        if node is None:
            keys = list(self.graph.keys())
            current_node = TreeNode(keys[0])
        else:
            current_node = node

        current_key = current_node.value
        for child, distance in self.graph[current_key].items():
            if distance != 0:
                current_node.add_child(child, distance)

        for child in current_node.children:
            if child.value not in child.get_ancestors():
                get_children = self.to_graph(child)
                child.children = get_children.children.copy()

        return current_node

    def __getitem__(self, item):
        return self.graph[item]
