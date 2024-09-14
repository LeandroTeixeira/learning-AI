from Common.Functions import get_node_action_path
from Common.treeNode import TreeNode


# TODO: BFS for graphs
def breadth_first_search_tree(tree: TreeNode, value):
    explored = []
    frontier = [tree]
    while len(frontier) > 0:
        current = frontier.pop(0)
        if current.value == value:
            return get_node_action_path(current)

        explored.append(current.value)

        for child in current.children:
            if child.value == value:
                return get_node_action_path(child)
            if child.value not in explored and child not in frontier:
                frontier.append(child)

    return None
