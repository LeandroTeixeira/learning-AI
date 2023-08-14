from Common.treeNode import TreeNode


def simple_depth_first_search(tree: TreeNode, value):
    if tree.value == value:
        return [tree.action]

    for child in tree.children:
        path = simple_depth_first_search(child, value)
        if path is not None:
            return [tree.action] + path

    return None
