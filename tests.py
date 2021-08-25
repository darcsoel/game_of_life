import unittest

from cell_strategy import (IsolatedStrategy, mutation_context,
                           OvercrowdingStrategy, ReproductionStrategy,
                           SurvivalStrategy)


class IsolatedStrategyTestCase(unittest.TestCase):
    def test_correct_case(self):
        strategy = IsolatedStrategy(True, 1)
        self.assertEqual(strategy.mutate(), False)

    def test_incorrect_case1(self):
        strategy = IsolatedStrategy(True, 3)
        with self.assertRaises(ValueError):
            strategy.mutate()

    def test_incorrect_case2(self):
        strategy = IsolatedStrategy(False, 3)
        with self.assertRaises(ValueError):
            strategy.mutate()


class SurvivalStrategyTestCase(unittest.TestCase):
    def test_correct_case1(self):
        strategy = SurvivalStrategy(True, 2)
        self.assertEqual(strategy.mutate(), True)

    def test_correct_case2(self):
        strategy = SurvivalStrategy(True, 3)
        self.assertEqual(strategy.mutate(), True)

    def test_incorrect_case1(self):
        strategy = SurvivalStrategy(False, 1)
        with self.assertRaises(ValueError):
            strategy.mutate()

    def test_incorrect_case2(self):
        strategy = SurvivalStrategy(False, 2)
        with self.assertRaises(ValueError):
            strategy.mutate()


class OvercrowdingStrategyTestCase(unittest.TestCase):
    def test_correct_case(self):
        strategy = OvercrowdingStrategy(True, 4)
        self.assertEqual(strategy.mutate(), False)

    def test_incorrect_case1(self):
        strategy = OvercrowdingStrategy(False, 4)
        with self.assertRaises(ValueError):
            strategy.mutate()

    def test_incorrect_case2(self):
        strategy = OvercrowdingStrategy(True, 2)
        with self.assertRaises(ValueError):
            strategy.mutate()


class ReproductionStrategyTestCase(unittest.TestCase):
    def test_correct_case(self):
        strategy = ReproductionStrategy(False, 3)
        self.assertEqual(strategy.mutate(), True)

    def test_incorrect_case1(self):
        strategy = ReproductionStrategy(False, 4)
        with self.assertRaises(ValueError):
            strategy.mutate()

    def test_incorrect_case2(self):
        strategy = ReproductionStrategy(True, 2)
        with self.assertRaises(ValueError):
            strategy.mutate()


class CheckMutationStrategy(unittest.TestCase):
    def test_isolation_strategy_case1(self):
        mutated = mutation_context(True, 1)
        self.assertEqual(mutated, False)


if __name__ == '__main__':
    unittest.main()
