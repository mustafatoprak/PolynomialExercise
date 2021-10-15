import unittest
from polynomialexercise.tests.unit.PolynomialExercise import TestPolynomialExercise
from polynomialexercise.tests.unit.PolynomialOperations import TestParamChecks, TestNumberSign, TestPolynomialOrder,\
    TestRandomNumberGenerator, TestPolyOpts, TestTerm, TestPolynomial, TestPolynomialOperations

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = unittest.TestLoader()

    # PolynomialExercise tests
    suite.addTests(tests.loadTestsFromTestCase(TestPolynomialExercise))

    # PolynomialOperations test
    suite.addTests(tests.loadTestsFromTestCase(TestParamChecks))
    suite.addTests(tests.loadTestsFromTestCase(TestNumberSign))
    suite.addTests(tests.loadTestsFromTestCase(TestPolynomialOrder))
    suite.addTests(tests.loadTestsFromTestCase(TestRandomNumberGenerator))
    suite.addTests(tests.loadTestsFromTestCase(TestPolyOpts))
    suite.addTests(tests.loadTestsFromTestCase(TestTerm))
    suite.addTests(tests.loadTestsFromTestCase(TestPolynomial))
    suite.addTests(tests.loadTestsFromTestCase(TestPolynomialOperations))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)