from Common.treeNode import TreeNode


def get_node_action_path(node: TreeNode):
    aux = node
    action_list = [aux.action]
    while aux.parent is not None:
        aux = aux.parent
        action_list = [aux.action] + action_list
    return action_list
