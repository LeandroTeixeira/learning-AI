from Common.treeNode import TreeNode


# TODO: BFS for graphs
def breadth_first_search_tree(tree: TreeNode, value):
    explored = []
    frontier = [tree]
    while len(frontier) > 0:
        current = frontier.pop(0)
        if current.value == value:
            aux = current
            action_list = [aux.action]
            while aux.parent is not None:
                aux = aux.parent
                action_list = [aux.action] + action_list
            return action_list

        explored.append(current.value)

        for child in current.children:
            if child.value not in explored and child not in frontier:
                frontier.append(child)

    return None
