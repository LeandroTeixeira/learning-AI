import unittest

from Agents.rules import Rules
from Common.LoggerSingleton import LoggerSingleton


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.states = [1, 2, 3, 4]
        self.actions = [lambda x: x, lambda x: x + 1, lambda x: x + 2, lambda x: x + 3]
        self.rule = Rules(self.states, self.actions)

    def test_initialization_success(self):
        rules_dict = self.rule.rules
        keys = rules_dict.keys()
        values = rules_dict.values()
        self.assertCountEqual(self.states, keys)
        self.assertCountEqual(self.actions, values)
        for key, value in zip(self.states, self.actions):
            self.assertEqual(rules_dict[key], value)

    def test_initialization_failure(self):
        def too_many_keys():
            states = [1, 2]
            actions = [lambda x: x]
            rule = Rules(states, actions)

        def too_many_values():
            states = [1, 2]
            actions = [lambda x: x, lambda x: x + 1, lambda x: x + 2, lambda x: x + 3]
            rule = Rules(states, actions)

        self.assertRaises(Exception, too_many_values, msg="There's not a direct match between state and actions!")
        self.assertRaises(Exception, too_many_keys, msg="There's not a direct match between state and actions!")

    def test_get_rule_success(self):
        for key, value in zip(self.states, self.actions):
            self.assertEqual(self.rule.get_action(key), value)

    def test_get_rule_failure(self):
        def get_wrong_rule():
            self.rule.get_action(-1)

        self.assertRaises(KeyError, get_wrong_rule)

    def tearDown(self) -> None:
        LoggerSingleton.print()


if __name__ == '__main__':
    unittest.main()
