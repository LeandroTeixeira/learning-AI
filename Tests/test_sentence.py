import unittest

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

        self.xor = Sentence("Xor", "Xor", {
            (a, b): (a or b) and not (a and b)
            for a in [True, False]
            for b in [True, False]
        })

        self.xnor = Sentence("Xnor", "Xnor", {
            (a, b): (a and b) or (not a and not b)
            for a in [True, False]
            for b in [True, False]
        })

        self.sentence_1 = Sentence("I went to a concert", "P", values=[False])
        self.sentence_2 = Sentence("I went to a football match", "Q", values=[False])
        self.sentence_3 = Sentence("I am in debt", "R", values=[False])

    def test_sentence_initialization(self):
        self.assertEqual(str(self.not_expr), "¬P")
        self.assertTrue(self.not_expr == self.not_2_expr)
        self.assertFalse(self.not_expr == self.and_expr)
        self.assertFalse(self.and_expr == self.and_3_expr)
        self.assertEqual(str(self.or_expr), "P v Q")
        self.assertEqual(str(self.and_expr), "P ^ Q")
        self.assertEqual(str(self.and_3_expr), "P ^ Q ^ R")
        self.assertEqual(str(self.xor), "P Xor Q")
        self.assertEqual(str(self.xnor), "P Xnor Q")

    def test_simple_eval_success(self):
        self.assertEqual(self.sentence_1(), False)
        self.assertEqual(self.sentence_2(), False)
        self.assertEqual(self.sentence_3(), False)

        self.assertEqual(self.not_expr(self.sentence_1), True)
        self.assertEqual(self.not_expr(self.sentence_2), True)
        self.assertEqual(self.not_expr(self.sentence_3), True)

        self.assertEqual(self.and_expr(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.and_expr(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.and_expr(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.or_expr(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.or_expr(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.or_expr(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.xor(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.xor(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.xor(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.xnor(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.xnor(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.xnor(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.and_3_expr(self.sentence_1, self.sentence_2, self.sentence_3), False)

        self.sentence_1.set(True)

        self.assertEqual(self.sentence_1(), True)
        self.assertEqual(self.sentence_2(), False)
        self.assertEqual(self.sentence_3(), False)

        self.assertEqual(self.not_expr(self.sentence_1), False)
        self.assertEqual(self.not_expr(self.sentence_2), True)
        self.assertEqual(self.not_expr(self.sentence_3), True)

        self.assertEqual(self.and_expr(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.and_expr(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.and_expr(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.or_expr(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.or_expr(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.or_expr(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.xor(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.xor(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.xor(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.xnor(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.xnor(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.xnor(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.and_3_expr(self.sentence_1, self.sentence_2, self.sentence_3), False)

        self.sentence_2.set(True)

        self.assertEqual(self.sentence_1(), True)
        self.assertEqual(self.sentence_2(), True)
        self.assertEqual(self.sentence_3(), False)

        self.assertEqual(self.not_expr(self.sentence_1), False)
        self.assertEqual(self.not_expr(self.sentence_2), False)
        self.assertEqual(self.not_expr(self.sentence_3), True)

        self.assertEqual(self.and_expr(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.and_expr(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.and_expr(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.or_expr(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.or_expr(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.or_expr(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.xor(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.xor(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.xor(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.xnor(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.xnor(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.xnor(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.and_3_expr(self.sentence_1, self.sentence_2, self.sentence_3), False)

        self.sentence_3.set(True)

        self.assertEqual(self.sentence_1(), True)
        self.assertEqual(self.sentence_2(), True)
        self.assertEqual(self.sentence_3(), True)

        self.assertEqual(self.not_expr(self.sentence_1), False)
        self.assertEqual(self.not_expr(self.sentence_2), False)
        self.assertEqual(self.not_expr(self.sentence_3), False)

        self.assertEqual(self.and_expr(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.and_expr(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.and_expr(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.or_expr(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.or_expr(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.or_expr(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.xor(self.sentence_1, self.sentence_2), False)
        self.assertEqual(self.xor(self.sentence_2, self.sentence_3), False)
        self.assertEqual(self.xor(self.sentence_3, self.sentence_1), False)

        self.assertEqual(self.xnor(self.sentence_1, self.sentence_2), True)
        self.assertEqual(self.xnor(self.sentence_2, self.sentence_3), True)
        self.assertEqual(self.xnor(self.sentence_3, self.sentence_1), True)

        self.assertEqual(self.and_3_expr(self.sentence_1, self.sentence_2, self.sentence_3), True)

        self.sentence_1.set(False)
        self.sentence_2.set(False)
        self.sentence_3.set(False)

    def test_combined_eval(self):
        self.not_expr.set(self.sentence_1)
        self.not_2_expr.set(self.sentence_2)
        self.and_expr.set(self.not_expr, self.not_2_expr)
        self.or_expr.set(self.not_expr, self.not_2_expr)
        self.xor.set(self.not_expr, self.not_2_expr)
        self.xnor.set(self.not_expr, self.not_2_expr)

        self.assertEqual(self.and_expr(), True)
        self.assertEqual(self.and_expr(True, False), False)
        self.assertEqual(self.or_expr(), True)
        self.assertEqual(self.xor(), False)
        self.assertEqual(self.xnor(), True)

        self.sentence_1.set(True)

        self.assertEqual(self.and_expr(), False)
        self.assertEqual(self.or_expr(), True)
        self.assertEqual(self.xor(), True)
        self.assertEqual(self.xnor(), False)

    def test_errors(self):
        def set_too_many_values():
            self.not_expr.set(self.sentence_1, self.sentence_2)

        def eval_too_many_values():
            self.and_expr.evaluate(self.sentence_1, self.sentence_2, self.sentence_3)

        def eval_too_few_values():
            self.or_expr.evaluate(self.sentence_1)

        def call_too_many_values():
            self.and_3_expr(self.sentence_3, self.sentence_2, self.sentence_1, self.sentence_2)

        self.assertRaises(Exception, set_too_many_values, "Invalid number of operators")
        self.assertRaises(Exception, eval_too_many_values, "Invalid number of operators")
        self.assertRaises(Exception, eval_too_few_values, "Invalid number of operators")
        self.assertRaises(Exception, call_too_many_values, "Invalid number of operators")


if __name__ == '__main__':
    unittest.main()
