# A dictionary that uses a default value when a key is not present
from collections import defaultdict

# Default value for when two vertices are not connected.
from Common.CONSTANTS import DEFAULT_NO_CONNECTION
from Common.treeNode import TreeNode


class Graph:
    def __init__(self, vertices: list, default_connection=DEFAULT_NO_CONNECTION):
        self.default_connection = default_connection
        # Default value set to an empty dictionary for properly implementing graph
        self.graph = defaultdict(dict)
        for vertice in vertices:
            for aux_vertice in vertices:
                self.graph[vertice][aux_vertice] = self.default_connection

    # Add connection between two vertices, creating new ones if any of them is not yet on the graph.
    def add_connection(self, src, target, value=1, directed=False):
        keys_list = list(self.graph.keys())
        if src not in keys_list:
            for key in keys_list:
                self.graph[src][key] = self.default_connection
                self.graph[key][src] = self.default_connection

        if target not in keys_list:
            for key in keys_list:
                self.graph[target][key] = self.default_connection
                self.graph[key][target] = self.default_connection

        self.graph[src][target] = value
        if not directed:
            self.graph[target][src] = value

        return self.graph

    def remove_connection(self, src, target, directed=False):
        self.graph[src][target] = self.default_connection
        if not directed:
            self.graph[target][src] = self.default_connection
        return self.graph

    def to_tree(self, node=None, action="go to"):
        # User can specify that root of the tree. If they don't, it is predefined as the first key.
        keys = list(self.graph.keys())
        current_node = node if node is not None else TreeNode(keys[0])

        # Add all the connected tiles as children
        current_key = current_node.value
        for child, distance in self.graph[current_key].items():
            if distance != self.default_connection:
                current_node.add_child(child, distance, action)

        # For each child not already included, convert to tree and append its children to the current tree.
        for child in current_node.children:
            if child.value not in child.get_ancestors():
                get_children = self.to_tree(child)
                child.children = get_children.children.copy()

        return current_node

    def print(self, default='-'):
        vertices = self.graph.keys()
        starting_line = '\t' + '\t'.join(map(str, vertices))
        print(starting_line)

        for v1 in vertices:
            line = [str(v1)]
            row = self.graph[v1]
            line.extend(str(row[v2]) if row[v2] != self.default_connection else default for v2 in row)
            print('\t'.join(line))
        print()

    def __getitem__(self, item):
        return self.graph[item]
