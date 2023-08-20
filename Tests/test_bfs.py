import unittest

from Common.treeNode import TreeNode
from Solving_Problems_by_Searching.Search_Algorithms.Breadth_First_Search import simple_breadth_first_search


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.test_tree = TreeNode(0, None, 0)
        self.test_tree.add_child(1, 1)
        self.test_tree.add_child(2, 1)
        self.test_tree.add_child(3, 1)
        self.test_tree.add_child(4, 1)
        self.test_tree.add_child(5, 1)
        self.test_tree.add_child(6, 1)
        self.test_tree.add_child(7, 1)
        self.test_tree.add_child(8, 1)
        repeated_node = TreeNode(9, self.test_tree, 1, "go to")
        self.test_tree.add_child_node(repeated_node)
        self.test_tree.add_child_node(repeated_node)
        self.test_tree.children[0].add_child(4, 1)
        self.test_tree.children[0].add_child(5, 1)
        self.test_tree.children[1].add_child(6, 1)
        self.test_tree.children[1].add_child(7, 1)
        self.test_tree.children[2].add_child(8, 1)
        self.test_tree.children[2].add_child(9, 1)
        self.test_tree.children[2].children[0].add_child(10, 1)

    def test_simple_search_success(self):
        path = ', '.join(simple_breadth_first_search(self.test_tree, 0))
        self.assertEqual(path, "Start at 0")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 1))
        self.assertEqual(path, "Start at 0, from 0, go to 1")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 2))
        self.assertEqual(path, "Start at 0, from 0, go to 2")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 3))
        self.assertEqual(path, "Start at 0, from 0, go to 3")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 4))
        self.assertEqual(path, "Start at 0, from 0, go to 4")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 5))
        self.assertEqual(path, "Start at 0, from 0, go to 5")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 6))
        self.assertEqual(path, "Start at 0, from 0, go to 6")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 7))
        self.assertEqual(path, "Start at 0, from 0, go to 7")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 8))
        self.assertEqual(path, "Start at 0, from 0, go to 8")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 9))
        self.assertEqual(path, "Start at 0, from 0, go to 9")
        path = ', '.join(simple_breadth_first_search(self.test_tree, 10))
        self.assertEqual(path, "Start at 0, from 0, go to 3, from 3, go to 8, from 8, go to 10")

    def test_simple_search_failure(self):
        value = 20
        path = simple_breadth_first_search(self.test_tree, value)
        self.assertIsNone(path, f"{value} is inside the tree and has the following path: {path}")


if __name__ == '__main__':
    unittest.main()
