from Intelligent_Agents.common.Rules import Rules
from common.LoggerSingleton import LoggerSingleton


class SimpleReflexAgent:

    def __init__(self, rules: Rules, name: str, interpreter):
        self.rules = rules
        self.name = name
        self.perception_interpreter = interpreter
        LoggerSingleton.log(f"Simple Reflex Agent {name} successfully Initialized")

    def act(self, perception):
        state = self.perception_interpreter(perception)
        return self.rules.get_action(state)


