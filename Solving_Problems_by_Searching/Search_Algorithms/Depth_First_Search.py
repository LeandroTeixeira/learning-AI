from Common.Functions import get_node_action_path
from Common.treeNode import TreeNode


# TODO: DFS for graphs
def depth_first_search_tree_iterative(tree: TreeNode, value):
    explored = []
    frontier = [tree]

    while len(frontier) > 0:
        current = frontier.pop(-1)
        if current.value == value:
            return get_node_action_path(current)

        explored.append(current.value)

        new_frontier = []
        for child in current.children:
            if child.value not in explored and child not in frontier:
                new_frontier.insert(0, child)

        frontier.extend(new_frontier)

    return None


def depth_first_search_tree_recursive(tree: TreeNode, value):
    if tree.value == value:
        return get_node_action_path(tree)

    for child in tree.children:
        return_value = depth_first_search_tree_iterative(child, value)
        if return_value is not None:
            return return_value

    return None
