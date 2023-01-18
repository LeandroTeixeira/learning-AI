import random

from Agents.rules import Rules
from Agents.simple_reflex_agent import SimpleReflexAgent
from Common.LoggerSingleton import LoggerSingleton


class BlackjackRules(Rules):
    def __init__(self):
        def hit(current_amount):
            LoggerSingleton.log("Getting another card")
            new_amount = random.randint(1, 10)
            LoggerSingleton.log(f"Got a card that's worth {new_amount}")
            return current_amount + new_amount

        def stop(current_amount):
            LoggerSingleton.log(f"Stopping with {current_amount}")
            return current_amount

        def win(current_amount):
            LoggerSingleton.log("Stopped with exactly 21!")
            return current_amount

        def bust(current_amount):
            LoggerSingleton.log(f"Busted with {current_amount}! I lost!")
            return current_amount

        states = ["Lower than 17", "Between 17 and 21", "21", "Above 21"]
        actions = [hit, stop, win, bust]
        super().__init__(states, actions)


class BlackjackAgent(SimpleReflexAgent):
    def __init__(self):
        def interpreter(value):
            if value < 17:
                return "Lower than 17"
            if value < 21:
                return "Between 17 and 21"
            if value == 21:
                return "21"
            if value > 21:
                return "Above 21"
        super().__init__(BlackjackRules(), "BlackJackAgent", interpreter)


def blackjack():
    s = BlackjackAgent()
    state = -1
    new_state = 0
    while new_state != state:
        state = new_state
        action = s.act(state)
        new_state = action(state)
