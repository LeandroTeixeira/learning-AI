class Sentence:
    def __init__(self, name, representation, eval_expression=None, values=None):
        if values is None:
            values = []
        if eval_expression is None:
            eval_expression = {True: True, False: False}
        self.name = name
        self.symbol = representation
        self.truth_table = eval_expression
        self.values = values
        if isinstance(list(self.truth_table.keys())[0], tuple):
            # noinspection PyTypeChecker
            self.n_operands = len(list(self.truth_table.keys())[0])
        else:
            self.n_operands = 1

    def set(self, *args):
        if len(args) != self.n_operands:
            raise Exception("Invalid number of operators")
        self.values = args

    def reset(self):
        self.values = []

    def evaluate(self, *args):
        if len(args) == 0:
            parameters = self.values
        else:
            parameters = args

        if len(parameters) != self.n_operands:
            raise Exception("Invalid number of operators")

        if self.n_operands == 1:
            return self.truth_table[parameters[0].evaluate() if isinstance(parameters[0], Sentence) else parameters[0]]
        # noinspection PyTypeChecker
        return self.truth_table[tuple(arg.evaluate() if isinstance(arg, Sentence) else arg for arg in parameters)]

    def __eq__(self, other):
        return set(self.truth_table) == set(other.truth_table)

    def __str__(self):
        if self.n_operands == 1:
            return self.symbol + "P"
        str_repr = "P"
        for i in range(1, self.n_operands):
            str_repr += f" {self.symbol} {value_to_letter_representation(i)}"
        return str_repr

    def __call__(self, *args):
        return self.evaluate(*args)


def value_to_letter_representation(value):
    if value < 0:
        return ""

    letters = "PQRSTUVW"
    num_letters = len(letters)

    return letters[value % num_letters] + str(value // num_letters) if value >= num_letters else letters[
        value % num_letters]
