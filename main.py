from Common.LoggerSingleton import LoggerSingleton
from Games.Blackjack import blackjack

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        blackjack()
    finally:
        LoggerSingleton.print()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
