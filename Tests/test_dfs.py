import unittest

from Common.graph import Graph
from Solving_Problems_by_Searching.Search_Algorithms.Depth_First_Search import depth_first_search_tree_iterative, \
    depth_first_search_tree_recursive


# TODO: Add tests for graph algorithm
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        # self.test_graph = Graph()
        self.test_graph = Graph([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.test_graph.add_connection(0, 1, 1, True)
        self.test_graph.add_connection(0, 2, 1, True)
        self.test_graph.add_connection(0, 3, 1, True)
        self.test_graph.add_connection(0, 4, 1, True)
        self.test_graph.add_connection(0, 5, 1, True)
        self.test_graph.add_connection(0, 6, 1, True)
        self.test_graph.add_connection(0, 7, 1, True)
        self.test_graph.add_connection(0, 9, 1, True)

        self.test_graph.add_connection(1, 4, 1, True)
        self.test_graph.add_connection(1, 5, 1, True)

        self.test_graph.add_connection(2, 6, 1, True)
        self.test_graph.add_connection(2, 7, 1, True)

        self.test_graph.add_connection(3, 8, 1, True)
        self.test_graph.add_connection(3, 9, 1, True)

        self.test_graph.add_connection(8, 10, 1, True)

        self.test_tree = self.test_graph.to_tree()
        #
        # self.test_tree = TreeNode(0, None, 0)
        #  self.test_tree.add_child(1, 1)
        #  self.test_tree.add_child(2, 1)
        #  self.test_tree.add_child(3, 1)
        #  self.test_tree.add_child(4, 1)
        #  self.test_tree.add_child(5, 1)
        #  self.test_tree.add_child(6, 1)
        #  self.test_tree.add_child(7, 1)
        #  repeated_node = TreeNode(9, self.test_tree, 1, "go to")
        #  self.test_tree.add_child_node(repeated_node)
        #  self.test_tree.add_child_node(repeated_node)
        #  self.test_tree.children[0].add_child(4, 1)
        #  self.test_tree.children[0].add_child(5, 1)
        #  self.test_tree.children[1].add_child(6, 1)
        #  self.test_tree.children[1].add_child(7, 1)
        #  self.test_tree.children[2].add_child(8, 1)
        #  self.test_tree.children[2].add_child(9, 1)
        #  self.test_tree.children[2].children[0].add_child(10, 1)

    def test_dfs_tree_success(self):
        answers = ["Start at 0", "Start at 0, from 0, go to 1", "Start at 0, from 0, go to 2",
                   "Start at 0, from 0, go to 3", "Start at 0, from 0, go to 1, from 1, go to 4",
                   "Start at 0, from 0, go to 1, from 1, go to 5", "Start at 0, from 0, go to 2, from 2, go to 6",
                   "Start at 0, from 0, go to 2, from 2, go to 7", "Start at 0, from 0, go to 3, from 3, go to 8",
                   "Start at 0, from 0, go to 3, from 3, go to 9",
                   "Start at 0, from 0, go to 3, from 3, go to 8, from 8, go to 10"]

        for i in range(0, 11):
            with self.subTest(name=f"DFS: {i}"):
                path = ', '.join(depth_first_search_tree_iterative(self.test_tree, i))
                self.assertEqual(answers[i], path)

                path = ', '.join(depth_first_search_tree_recursive(self.test_tree, i))
                self.assertEqual(answers[i], path)

    def test_dfs_tree_failure(self):
        value = 20
        path = depth_first_search_tree_iterative(self.test_tree, value)
        self.assertIsNone(path, f"{value} is inside the tree and has the following path: {path}")

        path = depth_first_search_tree_recursive(self.test_tree, value)
        self.assertIsNone(path, f"{value} is inside the tree and has the following path: {path}")

if __name__ == '__main__':
    unittest.main()
