import random

from Common.LoggerSingleton import LoggerSingleton
from Common.rules import Rules
from Simple_Reflex_Agents.simple_reflex_agent import SimpleReflexAgent


class BlackjackRules(Rules):
    def __init__(self):
        def hit(current_amount):
            print("Getting another card")
            new_amount = random.randint(1, 10)
            print(f"Got a card that's worth {new_amount}")
            return current_amount + new_amount

        def stop(current_amount):
            print(f"Stopping with {current_amount}")
            return current_amount

        def win(current_amount):
            print("Stopped with exactly 21!")
            return current_amount

        def bust(current_amount):
            print(f"Busted with {current_amount}! I lost!")
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        blackjack()
    finally:
        LoggerSingleton.print(console=False)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
