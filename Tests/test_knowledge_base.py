import copy
import unittest

from Knowledge.knowledge_base import KnowledgeBase
from Knowledge.sentence import Sentence


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.not_expr = Sentence("Not", "¬", {True: False, False: True})
        self.not_2_expr = Sentence("Not", "¬", {False: True, True: False})
        self.or_expr = Sentence("Or", "v",
                                {(a, b): a or b for a in [True, False] for b in [True, False]})
        self.and_expr = Sentence("And", "^",
                                 {(a, b): a and b for a in [True, False] for b in [True, False]})
        self.and_3_expr = Sentence("And³", "^",
                                   {(a, b, c): a and b and c
                                    for a in [True, False]
                                    for b in [True, False]
                                    for c in [True, False]})

        self.xor_expr = Sentence("Xor", "Xor", {
            (a, b): (a or b) and not (a and b)
            for a in [True, False]
            for b in [True, False]
        })

        self.conditional_expr = Sentence("Conditional", "->", {
            (a, b): (not a) or (a and b)
            for a in [True, False]
            for b in [True, False]
        })

        self.not_conditional_expr = Sentence("Conditional", "->", {
            (a, b): a or (not a and b)
            for a in [True, False]
            for b in [True, False]
        })

        self.biconditional_expr = Sentence("Biconditional", "<->", {
            (a, b): (a and b) or (not a and not b)
            for a in [True, False]
            for b in [True, False]
        })

        self.sentence_1 = Sentence("I went to a concert", "P", values=[True])
        self.sentence_2 = Sentence("I went to a football match", "Q", values=[True])
        self.sentence_3 = Sentence("I am in debt", "R", values=[True])

        self.kb_1 = KnowledgeBase([self.sentence_1, self.sentence_2, self.sentence_3],
                                  [self.biconditional_expr, self.not_expr],
                                  [(self.sentence_1, self.sentence_2), (self.sentence_3,)])

        self.kb_2 = KnowledgeBase([self.sentence_1, self.sentence_2, self.sentence_3],
                                  [copy.deepcopy(self.xor_expr),
                                   copy.deepcopy(self.xor_expr),
                                   copy.deepcopy(self.not_expr)],

                                  [(self.sentence_1, self.sentence_2),
                                   (self.sentence_1, self.sentence_3),
                                   (self.sentence_3,)])

        aux_not = copy.deepcopy(self.not_expr)
        aux_not.set(self.sentence_3)

        self.kb_3 = KnowledgeBase([self.sentence_1, self.sentence_2, self.sentence_3],
                                  [copy.deepcopy(self.not_conditional_expr),
                                   copy.deepcopy(self.biconditional_expr),
                                   copy.deepcopy(self.not_expr)],

                                  [(self.sentence_2, self.sentence_1),
                                   (self.sentence_3, self.sentence_2),
                                   (self.sentence_3,)])

    def test_initialization(self):
        logic = self.kb_1.logic
        premises = self.kb_1.premises
        self.assertDictEqual(premises, {"P": self.sentence_1, "Q": self.sentence_2, "R": self.sentence_3})
        self.assertListEqual(list(logic.keys()), ["P <-> Q", "¬R"])
        self.assertListEqual([value.evaluate() for _, value in logic.items()], [True, False])

    def test_model_checking(self):
        self.assertEqual(self.kb_2.entails_by_model_checking(self.sentence_1), True)
        self.assertEqual(self.kb_2.entails_by_model_checking(self.sentence_2), False)
        self.assertEqual(self.kb_2.entails_by_model_checking(self.sentence_3), False)

        self.assertEqual(self.kb_3.entails_by_model_checking(self.sentence_1), True)
        self.assertEqual(self.kb_3.entails_by_model_checking(self.sentence_2), False)
        self.assertEqual(self.kb_3.entails_by_model_checking(self.sentence_3), False)


if __name__ == '__main__':
    unittest.main()
