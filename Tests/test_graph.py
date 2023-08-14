import random
import unittest

from Common.CONSTANTS import DEFAULT_NO_CONNECTION
from Common.graph import Graph


# TODO: Test cases with action variable
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.starting_cities = ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia", "Porto Alegre", "Curitiba"]
        self.main_graph = Graph(self.starting_cities, DEFAULT_NO_CONNECTION)

    def test_graph_initialization(self):
        graph = self.main_graph.graph
        self.assertCountEqual(graph.keys(), self.starting_cities)
        for value in graph.values():
            self.assertCountEqual(value, self.starting_cities)

        for city_1 in self.starting_cities:
            for city_2 in self.starting_cities:
                value = self.main_graph[city_1][city_2]
                self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)

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
                        self.assertEqual(value, DEFAULT_NO_CONNECTION)
                    else:
                        self.assertEqual(value, 1)

    def test_to_tree_non_circular(self):
        non_circular_graph = Graph(
            ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia", "Porto Alegre", "Curitiba"])
        # ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia", "Porto Alegre", "Curitiba"]
        # Expected Graph:
        # 0 1 1 0 0 0
        # 0 0 0 0 0 0
        # 0 0 0 1 0 1
        # 0 1 0 0 0 0
        # 0 1 0 0 0 0
        # 0 1 0 0 1 0
        non_circular_graph.add_connection("Belo Horizonte", "São Paulo", directed=True)
        non_circular_graph.add_connection("Belo Horizonte", "Rio de Janeiro", directed=True)
        non_circular_graph.add_connection("Rio de Janeiro", "Brasilia", directed=True)
        non_circular_graph.add_connection("Rio de Janeiro", "Curitiba", directed=True)
        non_circular_graph.add_connection("Brasilia", "São Paulo", directed=True)
        non_circular_graph.add_connection("Porto Alegre", "São Paulo", directed=True)
        non_circular_graph.add_connection("Curitiba", "Porto Alegre", directed=True)
        non_circular_graph.add_connection("Curitiba", "São Paulo", directed=True)

        tree = non_circular_graph.to_tree()
        self.assertEqual(tree.value, "Belo Horizonte")
        self.assertCountEqual([child.value for child in tree.children], ["São Paulo", "Rio de Janeiro"])

        sao_paulo = tree.children[0] if tree.children[0].value == "São Paulo" else tree.children[1]
        self.assertEqual(sao_paulo.value, "São Paulo")
        self.assertEqual(len(sao_paulo.children), 0)
        rio_de_janeiro = tree.children[0] if tree.children[0].value == "Rio de Janeiro" else tree.children[1]
        self.assertEqual(rio_de_janeiro.value, "Rio de Janeiro")
        self.assertCountEqual([child.value for child in rio_de_janeiro.children], ["Brasilia", "Curitiba"])

        brasilia = rio_de_janeiro.children[0] if rio_de_janeiro.children[0].value == "Brasilia" \
            else rio_de_janeiro.children[1]
        curitiba = rio_de_janeiro.children[0] if rio_de_janeiro.children[0].value == "Curitiba" \
            else rio_de_janeiro.children[1]

        self.assertEqual(brasilia.value, "Brasilia")
        self.assertCountEqual([child.value for child in brasilia.children], ["São Paulo"])
        self.assertEqual(curitiba.value, "Curitiba")
        self.assertCountEqual([child.value for child in curitiba.children], ["Porto Alegre", "São Paulo"])

        sao_paulo = curitiba.children[0] if curitiba.children[0].value == "São Paulo" else curitiba.children[1]
        self.assertEqual(sao_paulo.value, "São Paulo")
        self.assertEqual(len(sao_paulo.children), 0)
        porto_alegre = curitiba.children[0] if curitiba.children[0].value == "Porto Alegre" else curitiba.children[1]
        self.assertEqual(porto_alegre.value, "Porto Alegre")
        self.assertCountEqual([child.value for child in porto_alegre.children], ["São Paulo"])

    def test_to_tree_circular(self):

        circular_graph = Graph(
            ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia", "Porto Alegre", "Curitiba"])
        # ["Belo Horizonte", "São Paulo", "Rio de Janeiro", "Brasilia", "Porto Alegre", "Curitiba"]
        # Expected Graph:
        # 0 0 1 0 0 1
        # 1 0 0 0 0 1
        # 0 1 0 1 0 0
        # 1 0 1 0 0 0
        # 0 1 0 0 1 0
        # 0 0 0 1 1 0
        circular_graph.add_connection("Belo Horizonte", "Rio de Janeiro", directed=True)
        circular_graph.add_connection("Belo Horizonte", "Curitiba", directed=True)
        circular_graph.add_connection("São Paulo", "Belo Horizonte", directed=True)
        circular_graph.add_connection("São Paulo", "Curitiba", directed=True)
        circular_graph.add_connection("Rio de Janeiro", "São Paulo", directed=True)
        circular_graph.add_connection("Rio de Janeiro", "Brasilia", directed=True)
        circular_graph.add_connection("Brasilia", "Rio de Janeiro", directed=True)
        circular_graph.add_connection("Brasilia", "Belo Horizonte", directed=True)
        circular_graph.add_connection("Porto Alegre", "São Paulo", directed=True)
        circular_graph.add_connection("Porto Alegre", "Porto Alegre", directed=True)
        circular_graph.add_connection("Curitiba", "Porto Alegre", directed=True)
        circular_graph.add_connection("Curitiba", "Brasilia", directed=True)

        tree = circular_graph.to_tree()
        self.assertEqual(tree.value, "Belo Horizonte")
        self.assertCountEqual([child.value for child in tree.children], ["Curitiba", "Rio de Janeiro"])

        curitiba_1 = tree.children[0] if tree.children[0].value == "Curitiba" else tree.children[1]
        self.assertEqual(curitiba_1.value, "Curitiba")
        self.assertCountEqual([child.value for child in curitiba_1.children], ["Brasilia", "Porto Alegre"])
        rio_de_janeiro_1 = tree.children[0] if tree.children[0].value == "Rio de Janeiro" else tree.children[1]
        self.assertEqual(rio_de_janeiro_1.value, "Rio de Janeiro")
        self.assertCountEqual([child.value for child in rio_de_janeiro_1.children], ["Brasilia", "São Paulo"])

        porto_alegre_1 = curitiba_1.children[0] if curitiba_1.children[0].value == "Porto Alegre" \
            else curitiba_1.children[1]
        self.assertEqual(porto_alegre_1.value, "Porto Alegre")
        self.assertCountEqual([child.value for child in porto_alegre_1.children], ["São Paulo", "Porto Alegre"])
        brasilia_1 = curitiba_1.children[0] if curitiba_1.children[0].value == "Brasilia" else curitiba_1.children[1]
        self.assertEqual(brasilia_1.value, "Brasilia")
        self.assertCountEqual([child.value for child in brasilia_1.children], ["Rio de Janeiro", "Belo Horizonte"])

        sao_paulo_1 = rio_de_janeiro_1.children[0] if rio_de_janeiro_1.children[0].value == "São Paulo" \
            else rio_de_janeiro_1.children[1]
        self.assertEqual(sao_paulo_1.value, "São Paulo")
        self.assertCountEqual([child.value for child in sao_paulo_1.children], ["Belo Horizonte", "Curitiba"])
        brasilia_2 = rio_de_janeiro_1.children[0] if rio_de_janeiro_1.children[0].value == "Brasilia" \
            else rio_de_janeiro_1.children[1]
        self.assertEqual(brasilia_2.value, "Brasilia")
        self.assertCountEqual([child.value for child in brasilia_2.children], ["Rio de Janeiro", "Belo Horizonte"])

        sao_paulo_2 = porto_alegre_1.children[0] if porto_alegre_1.children[0].value == "São Paulo" \
            else porto_alegre_1.children[1]
        self.assertEqual(sao_paulo_2.value, "São Paulo")
        self.assertCountEqual([child.value for child in sao_paulo_2.children], ["Belo Horizonte", "Curitiba"])
        porto_alegre_2 = porto_alegre_1.children[0] if porto_alegre_1.children[0].value == "Porto Alegre" \
            else porto_alegre_1.children[1]
        self.assertEqual(porto_alegre_2.value, "Porto Alegre")
        self.assertEqual(len(porto_alegre_2.children), 0)

        rio_de_janeiro_2 = brasilia_1.children[0] if brasilia_1.children[0].value == "Rio de Janeiro" \
            else brasilia_1.children[1]
        self.assertEqual(rio_de_janeiro_2.value, "Rio de Janeiro")
        self.assertCountEqual([child.value for child in rio_de_janeiro_2.children], ["Brasilia", "São Paulo"])
        belo_horizonte_1 = brasilia_1.children[0] if brasilia_1.children[0].value == "Belo Horizonte" \
            else brasilia_1.children[1]
        self.assertEqual(belo_horizonte_1.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_1.children), 0)

        rio_de_janeiro_3 = brasilia_2.children[0] if brasilia_2.children[0].value == "Rio de Janeiro" \
            else brasilia_2.children[1]
        self.assertEqual(rio_de_janeiro_3.value, "Rio de Janeiro")
        self.assertEqual(len(rio_de_janeiro_3.children), 0)
        belo_horizonte_2 = brasilia_2.children[0] if brasilia_2.children[0].value == "Belo Horizonte" \
            else brasilia_2.children[1]
        self.assertEqual(belo_horizonte_2.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_2.children), 0)

        curitiba_2 = sao_paulo_1.children[0] if sao_paulo_1.children[0].value == "Curitiba" \
            else sao_paulo_1.children[1]
        self.assertEqual(curitiba_2.value, "Curitiba")
        self.assertCountEqual([child.value for child in curitiba_2.children], ["Porto Alegre", "Brasilia"])
        belo_horizonte_3 = sao_paulo_1.children[0] if sao_paulo_1.children[0].value == "Belo Horizonte" \
            else sao_paulo_1.children[1]
        self.assertEqual(belo_horizonte_3.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_3.children), 0)

        curitiba_3 = sao_paulo_2.children[0] if sao_paulo_2.children[0].value == "Curitiba" \
            else sao_paulo_2.children[1]
        self.assertEqual(curitiba_3.value, "Curitiba")
        self.assertEqual(len(curitiba_3.children), 0)
        belo_horizonte_4 = sao_paulo_2.children[0] if sao_paulo_2.children[0].value == "Belo Horizonte" \
            else sao_paulo_2.children[1]
        self.assertEqual(belo_horizonte_4.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_4.children), 0)

        sao_paulo_3 = rio_de_janeiro_2.children[0] if rio_de_janeiro_2.children[0].value == "São Paulo" \
            else rio_de_janeiro_2.children[1]
        self.assertEqual(sao_paulo_3.value, "São Paulo")
        self.assertCountEqual([child.value for child in sao_paulo_3.children], ["Belo Horizonte", "Curitiba"])
        brasilia_3 = rio_de_janeiro_2.children[0] if rio_de_janeiro_2.children[0].value == "Brasilia" \
            else rio_de_janeiro_2.children[1]
        self.assertEqual(brasilia_3.value, "Brasilia")
        self.assertEqual(len(brasilia_3.children), 0)

        porto_alegre_3 = curitiba_2.children[0] if curitiba_2.children[0].value == "Porto Alegre" \
            else curitiba_2.children[1]
        self.assertEqual(porto_alegre_3.value, "Porto Alegre")
        self.assertCountEqual([child.value for child in porto_alegre_3.children], ["São Paulo", "Porto Alegre"])
        brasilia_4 = curitiba_2.children[0] if curitiba_2.children[0].value == "Brasilia" else curitiba_2.children[1]
        self.assertEqual(brasilia_4.value, "Brasilia")
        self.assertCountEqual([child.value for child in brasilia_4.children], ["Rio de Janeiro", "Belo Horizonte"])

        curitiba_4 = sao_paulo_3.children[0] if sao_paulo_3.children[0].value == "Curitiba" \
            else sao_paulo_3.children[1]
        self.assertEqual(curitiba_4.value, "Curitiba")
        self.assertEqual(len(curitiba_4.children), 0)
        belo_horizonte_5 = sao_paulo_3.children[0] if sao_paulo_3.children[0].value == "Belo Horizonte" \
            else sao_paulo_3.children[1]
        self.assertEqual(belo_horizonte_5.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_5.children), 0)

        sao_paulo_4 = porto_alegre_3.children[0] if porto_alegre_3.children[0].value == "São Paulo" \
            else porto_alegre_3.children[1]
        self.assertEqual(sao_paulo_4.value, "São Paulo")
        self.assertEqual(len(sao_paulo_4.children), 0)
        porto_alegre_4 = porto_alegre_3.children[0] if porto_alegre_3.children[0].value == "Porto Alegre" \
            else porto_alegre_3.children[1]
        self.assertEqual(porto_alegre_4.value, "Porto Alegre")
        self.assertEqual(len(porto_alegre_4.children), 0)

        rio_de_janeiro_4 = brasilia_4.children[0] if brasilia_4.children[0].value == "Rio de Janeiro" \
            else brasilia_4.children[1]
        self.assertEqual(rio_de_janeiro_4.value, "Rio de Janeiro")
        self.assertEqual(len(rio_de_janeiro_4.children), 0)
        belo_horizonte_6 = brasilia_4.children[0] if brasilia_4.children[0].value == "Belo Horizonte" \
            else brasilia_4.children[1]
        self.assertEqual(belo_horizonte_6.value, "Belo Horizonte")
        self.assertEqual(len(belo_horizonte_6.children), 0)


if __name__ == '__main__':
    unittest.main()
