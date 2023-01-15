class LoggerSingleton:
    __log = ""

    def __init__(self):
        if LoggerSingleton.__log is None:
            LoggerSingleton.__log = ""

    @staticmethod
    def get():
        return LoggerSingleton.__log

    @staticmethod
    def print():
        print(LoggerSingleton.__log)
        with open('log.txt', 'w') as f:
            f.write(LoggerSingleton.__log)

    @staticmethod
    def log(text):
        LoggerSingleton.__log += text + "\n"

    @staticmethod
    def reset():
        LoggerSingleton.__log = ""
