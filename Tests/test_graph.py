import random
import unittest

from Common.graph import Graph


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.starting_cities = ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia"]
        self.main_graph = Graph(self.starting_cities)

    def test_graph_initialization(self):
        graph = self.main_graph.graph
        self.assertCountEqual(graph.keys(), self.starting_cities)
        for value in graph.values():
            self.assertCountEqual(value, self.starting_cities)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                value = self.main_graph[city_1][city_2]
                self.assertEqual(value, 0)

    def test_unidirectional_input(self):
        main_city = self.starting_cities[0]
        for city in self.starting_cities:
            self.main_graph.add_connection(city, main_city, directed=True)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_2 == main_city:
                        self.assertEqual(value, 1)
                    else:
                        self.assertEqual(value, 0)

    def test_unidirectional_input_different_value(self):
        main_city = self.starting_cities[0]
        expected_value = random.randint(1, 100)
        for city in self.starting_cities:
            self.main_graph.add_connection(city, main_city, expected_value, directed=True)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_2 == main_city:
                        self.assertEqual(value, expected_value)
                    else:
                        self.assertEqual(value, 0)

    def test_unidirectional_input_new_data(self):
        new_city_1 = "Salvador"
        new_city_2 = "Vitória"
        updated_list = self.starting_cities.copy()

        updated_list.append(new_city_1)
        for city in updated_list:
            self.main_graph.add_connection(city, new_city_1, directed=True)

        updated_list.append(new_city_2)
        for city in updated_list:
            self.main_graph.add_connection(new_city_2, city, directed=True)

        for city_1 in updated_list:
            for city_2 in updated_list:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_1 == new_city_2 or city_2 == new_city_1:
                        self.assertEqual(value, 1)
                    else:
                        self.assertEqual(value, 0)

    def test_bidirectional_input_different_value(self):
        main_city = self.starting_cities[0]
        expected_value = random.randint(1, 100)

        for city in self.starting_cities:
            self.main_graph.add_connection(city, main_city, expected_value)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_2 == main_city or city_1 == main_city:
                        self.assertEqual(value, expected_value)
                    else:
                        self.assertEqual(value, 0)

    def test_bidirectional_input(self):
        main_city = self.starting_cities[0]
        expected_value = 1

        for city in self.starting_cities:
            self.main_graph.add_connection(city, main_city)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_2 == main_city or city_1 == main_city:
                        self.assertEqual(value, expected_value)
                    else:
                        self.assertEqual(value, 0)

    def test_bidirectional_input_new_data(self):
        new_city_1 = "Salvador"
        new_city_2 = "Vitória"
        updated_list = self.starting_cities.copy()

        updated_list.append(new_city_1)
        for city in updated_list:
            self.main_graph.add_connection(city, new_city_1)

        updated_list.append(new_city_2)
        for city in updated_list:
            self.main_graph.add_connection(new_city_2, city)

        for city_1 in updated_list:
            for city_2 in updated_list:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = self.main_graph[city_1][city_2]
                    if city_1 == new_city_1 or city_1 == new_city_2 or city_2 == new_city_1 or city_2 == new_city_2:
                        self.assertEqual(value, 1)
                    else:
                        self.assertEqual(value, 0)

    def test_removal_unidirectional(self):
        populated_graph = Graph(self.starting_cities)
        c1 = self.starting_cities[0]
        c2 = self.starting_cities[1]

        populated_graph.add_connection(c1, c2)
        populated_graph.remove_connection(c1, c2, directed=True)
        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = populated_graph[city_1][city_2]
                    if city_2 == c1 and city_1 == c2:
                        self.assertEqual(value, 1)
                    else:
                        self.assertEqual(value, 0)

    def test_removal_bidirectional(self):
        populated_graph = Graph(self.starting_cities)
        c1 = self.starting_cities[0]
        c2 = self.starting_cities[1]
        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                populated_graph.add_connection(city_1, city_2)

        populated_graph.remove_connection(c1, c2)
        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                with self.subTest(name=f"C1: {city_1} C2: {city_2}"):
                    value = populated_graph[city_1][city_2]
                    if (city_2 == c1 and city_1 == c2) or (city_1 == c1 and city_2 == c2):
                        self.assertEqual(value, 0)
                    else:
                        self.assertEqual(value, 1)


if __name__ == '__main__':
    unittest.main()
