from Common.LoggerSingleton import LoggerSingleton


class Rules:

    def __init__(self, states: list, actions: list):
        if len(states) != len(actions):
            LoggerSingleton.log(f"Number of states: {len(states)}\t Number of actions {len(actions)}")
            raise Exception("There's not a direct match between state and actions!")
        self.rules = dict()
        for state, action in zip(states, actions):
            self.rules[state] = action
        LoggerSingleton.log("Rules successfully initialized")

    def get_action(self, state):
        rule = self.rules[state]
        return rule

