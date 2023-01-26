import unittest

from Common.loggerSingleton import LoggerSingleton
from Common.rules import Rules
from Simple_Reflex_Agents.simple_reflex_agent import SimpleReflexAgent


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.rules = ["Even", "Odd"]
        self.actions = [lambda: "It's even", lambda: "It's odd"]
        self.ruleset = Rules(self.rules, self.actions)
        self.interpreter = lambda x: "Even" if x % 2 == 0 else "Odd"
        self.test_cases = [i for i in range(0, 10)]

    def test_initialization(self):
        name = "Test_Agent"
        agent = SimpleReflexAgent(self.ruleset, name, self.interpreter)
        self.assertEqual(agent.rules, self.ruleset)
        self.assertEqual(agent.name, name)
        self.assertEqual(agent.perception_interpreter, self.interpreter)

    def test_actions(self):
        agent = SimpleReflexAgent(self.ruleset, "Test_Agent", self.interpreter)
        for test in self.test_cases:
            action = self.ruleset.get_action(self.interpreter(test))
            agent_action = agent.act(test)
            self.assertEqual(action, agent_action)

    def tearDown(self) -> None:
        LoggerSingleton.print(console=False)


if __name__ == '__main__':
    unittest.main()
