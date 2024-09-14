from Common.treeNode import TreeNode
from Solving_Problems_by_Searching.Common import get_node_action_path


# TODO: DFS for graphs
def depth_first_search_tree(tree: TreeNode, value):
    explored = []
    frontier = [tree]

    while len(frontier) > 0:
        current = frontier.pop(-1)
        if current.value == value:
            return get_node_action_path(current)

        explored.append(current.value)

        for child in reversed(current.children):
            if child.value not in explored and child not in frontier:
                frontier.append(child)

    return None
