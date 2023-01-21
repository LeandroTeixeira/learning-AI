from Common.LoggerSingleton import LoggerSingleton
from Common.rules import Rules


class SimpleReflexAgent:

    def __init__(self, rules: Rules, name: str, interpreter):
        self.rules = rules
        self.name = name
        self.perception_interpreter = interpreter
        LoggerSingleton.log(f"Simple Reflex Agent {name} successfully Initialized")

    def act(self, perception):
        LoggerSingleton.log(f"Agent {self.name}: Received perception {perception}")
        state = self.perception_interpreter(perception)
        LoggerSingleton.log(f"Agent {self.name}: Corresponding state is {state}")
        action = self.rules.get_action(state)
        LoggerSingleton.log(f"Agent {self.name}: Retrieved function {action.__name__}")
        return action
