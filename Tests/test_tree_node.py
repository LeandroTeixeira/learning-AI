import unittest

from Common.treeNode import TreeNode


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.create_node_value = "Root"
        self.node = TreeNode(self.create_node_value)
        self.children = [
            {"value": "First Child", "distance": 1},
            {"value": "Second Child", "distance": 2},
            {"value": "Third Child", "distance": 3}
        ]

    def test_creating_node(self):
        self.assertEqual(self.node.value, self.create_node_value)
        self.assertEqual(self.node.distance, 0)
        self.assertEqual(self.node.parent, None)
        self.assertEqual(self.node.children, [])

    def test_adding_children_wide(self):
        for child in self.children:
            self.node.add_child(child["value"], child["distance"])

        children = self.node.children
        self.assertEqual(len(children), len(self.children))
        for got, expected in zip(children, self.children):
            with self.subTest(name=expected["value"]):
                self.assertEqual(got.value, expected["value"])
                self.assertEqual(got.distance, expected["distance"])
                self.assertEqual(got.parent, self.node)

    def test_adding_children_deep_distance(self):
        current_node = self.node
        for child in self.children:
            current_node.add_child(child["value"], child["distance"])
            current_node = current_node.children[0]
        current_node.add_child(None, 0)
        current_node = self.node
        distance = self.node.distance
        self.assertEqual(len(current_node.children), 1)
        self.assertEqual(self.create_node_value, current_node.value)
        self.assertEqual(distance, current_node.get_distance_from_root())
        current_node = current_node.children[0]
        for expected in self.children:
            with self.subTest(name=current_node.value):
                distance += current_node.distance
                self.assertEqual(len(current_node.children), 1)
                self.assertEqual(expected["distance"], current_node.distance)
                self.assertEqual(expected["value"], current_node.value)
                self.assertEqual(distance, current_node.get_distance_from_root())

                current_node = current_node.children[0]

    def test_ancestor(self):
        current_node = self.node
        for child in self.children:
            current_node.add_child(child["value"], child["distance"])
            current_node = current_node.children[0]
        current_node.add_child("Tester")
        current_node = current_node.children[0]
        ancestors = [child["value"] for child in self.children]
        ancestors.append(self.node.value)
        self.assertCountEqual(current_node.get_ancestors(), ancestors)

    def tearDown(self) -> None:
        self.node.children = []


if __name__ == '__main__':
    unittest.main()
