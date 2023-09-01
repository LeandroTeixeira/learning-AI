import copy
from itertools import product

from Knowledge.sentence import Sentence


class KnowledgeBase:
    def __init__(self, premises: [Sentence], operators: [Sentence], operands: [Sentence]):
        self.premises = {premise.symbol: copy.deepcopy(premise) for premise in premises}
        self.logic = dict()
        if len(operators) != len(operands):
            raise Exception("Operators and operands do not match!")

        for operator, operand in zip(operators, operands):
            operator.set(*(self.premises[v.symbol] for v in operand))
            self.logic[str(operator)] = operator

    def entails_by_model_checking(self, alpha: Sentence):
        if alpha.symbol not in self.premises:
            raise Exception("Premise not found!")

        for permutations in product([True, False], repeat=len(self.premises)):
            for premise, permutation in zip(self.premises.values(), permutations):
                premise.set(permutation)

            implications = []
            for value in self.logic.values():
                implications.append(value.evaluate())

            if implications.count(False) == 0:
                if self.premises[alpha.symbol].values[0] != alpha.values[0]:
                    return False
        return True
