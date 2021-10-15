import unittest
from polynomialexercise.tests.unit.PolynomialExercise import TestPolynomialExercise


def load_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(TestPolynomialExercise))
    # suite.addTests(loader.loadTestsFromModule(PolynomialOperations))
    return suite


if __name__ == '__main__':
    suite_tests = load_tests()
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite_tests)