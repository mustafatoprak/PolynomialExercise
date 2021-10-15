import unittest
from polynomialexercise.sources.PolynomialOperations import _check_if_params_none,_check_if_params_smaller_or_greater_than_a_value
from polynomialexercise.sources.PolynomialOperations import NumberSign, PolynomialOrder, RandomNumberGenerator, PolyOpts, Term,\
    Polynomial, PolynomialOperations


######################################################################################
class TestParamChecks(unittest.TestCase):
    def test__check_if_params_none(self):
        self.assertTrue(_check_if_params_none(params=[1, 2, None]))
        self.assertFalse(_check_if_params_none(params=[1, 2, -5]))

    def test__check_if_params_smaller_or_greater_than_a_value(self):
        # all
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[-1, 3, 4], value=5, operation="lt"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[-1, 3, 5], value=5, operation="lte"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[7, 8, 10], value=6, operation="gt"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[11, 9, 6], value=6, operation="gte"))
        self.assertFalse(_check_if_params_smaller_or_greater_than_a_value(params=[-1, 3, 5], value=5, operation="lt"))
        self.assertFalse(_check_if_params_smaller_or_greater_than_a_value(params=[-1, 3, 6], value=5, operation="lte"))
        self.assertFalse(_check_if_params_smaller_or_greater_than_a_value(params=[7, 8, 6], value=6, operation="gt"))
        self.assertFalse(_check_if_params_smaller_or_greater_than_a_value(params=[11, 9, 5], value=6, operation="gte"))
        # any
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[-1, 5, 6], value=5, operation="lt", type="any"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[5, 7, 7], value=5, operation="lte", type="any"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[5, 4, 10], value=6, operation="gt", type="any"))
        self.assertTrue(_check_if_params_smaller_or_greater_than_a_value(params=[3, 6, 6], value=6, operation="gte", type="any"))

    def test__check_if_params_smaller_or_greater_than_a_value_exceptions(self):
        self.assertRaises(ValueError,
                          _check_if_params_smaller_or_greater_than_a_value, params=[-1, 3, 4], value=5, operation="xxx")

######################################################################################
class TestNumberSign(unittest.TestCase):
    def test_enum_numbers(self):
        self.assertEqual(NumberSign.NEG.value, 1)
        self.assertEqual(NumberSign.POS.value, 2)
        self.assertEqual(NumberSign.ZERO.value, 3)


######################################################################################
class TestPolynomialOrder(unittest.TestCase):
    def test_enum_numbers(self):
        self.assertEqual(PolynomialOrder.ASC.value, 1)
        self.assertEqual(PolynomialOrder.DESC.value, 2)
        self.assertEqual(PolynomialOrder.UNORDERED.value, 3)


######################################################################################
class TestRandomNumberGenerator(unittest.TestCase):
    def test_enum_numbers(self):
        random_number_generator = RandomNumberGenerator()
        self.assertTrue(2 <= random_number_generator.generate_random_number(2, 5) <= 5)
        self.assertTrue(-2 <= random_number_generator.generate_random_number(-2, 0) <= 0)

    def test_enum_numbers_exceptions(self):
        random_number_generator = RandomNumberGenerator()
        self.assertRaises(ValueError, random_number_generator.generate_random_number, min_value=2, max_value=None)
        self.assertRaises(ValueError, random_number_generator.generate_random_number, min_value=None, max_value=5)
        self.assertRaises(ValueError, random_number_generator.generate_random_number, min_value=7, max_value=5)


######################################################################################
class TestPolyOpts(unittest.TestCase):
    def test_default_values(self):
        polyOpts = PolyOpts()
        self.assertEqual(polyOpts.min_num_of_terms_in_poly, 2)
        self.assertEqual(polyOpts.max_num_of_terms_in_poly, 4)
        self.assertListEqual(polyOpts.term_num_per_poly, [2, 4])
        self.assertEqual(polyOpts.min_coefficient_value, -12)
        self.assertEqual(polyOpts.max_coefficient_value, 12)
        self.assertEqual(polyOpts.min_exponential_value, 1)
        self.assertEqual(polyOpts.max_exponential_value, 5)
        self.assertListEqual(polyOpts.variable_letters, ["x", "y", "z", "a", "b", "c"])

    def test_setting_values(self):
        polyOpts = PolyOpts()
        polyOpts.min_num_of_terms_in_poly = 1
        self.assertEqual(polyOpts.min_num_of_terms_in_poly, 1)
        polyOpts.max_num_of_terms_in_poly = 2
        self.assertEqual(polyOpts.max_num_of_terms_in_poly, 2)
        polyOpts.term_num_per_poly = [1, 2, 3, 4, 5]
        self.assertListEqual(polyOpts.term_num_per_poly, [1, 2, 3, 4, 5])
        polyOpts.min_coefficient_value = 3
        self.assertEqual(polyOpts.min_coefficient_value, 3)
        polyOpts.max_coefficient_value = 4
        self.assertEqual(polyOpts.max_coefficient_value, 4)
        polyOpts.min_exponential_value = 5
        self.assertEqual(polyOpts.min_exponential_value, 5)
        polyOpts.max_exponential_value = 6
        self.assertEqual(polyOpts.max_exponential_value, 6)
        polyOpts.variable_letters = ["a", "b", "c"]
        self.assertListEqual(polyOpts.variable_letters, ["a", "b", "c"])

    def test_setting_values_exceptions(self):
        self.assertRaises(ValueError, PolyOpts, min_num_of_terms_in_poly=-1)
        self.assertRaises(ValueError, PolyOpts, max_num_of_terms_in_poly=-1)
        self.assertRaises(ValueError, PolyOpts, min_num_of_terms_in_poly=2, max_num_of_terms_in_poly=1)
        self.assertRaises(ValueError, PolyOpts, min_coefficient_value=2, max_coefficient_value=1)
        self.assertRaises(ValueError, PolyOpts, min_exponential_value=-1)
        self.assertRaises(ValueError, PolyOpts, max_exponential_value=-1)
        self.assertRaises(ValueError, PolyOpts, min_exponential_value=2, max_exponential_value=1)
        self.assertRaises(ValueError, PolyOpts, min_num_of_terms_in_poly=None)
        self.assertRaises(ValueError, PolyOpts, max_num_of_terms_in_poly=None)
        self.assertRaises(ValueError, PolyOpts, term_num_per_poly=None)
        self.assertRaises(ValueError, PolyOpts, min_coefficient_value=None)
        self.assertRaises(ValueError, PolyOpts, max_coefficient_value=None)
        self.assertRaises(ValueError, PolyOpts, min_exponential_value=None)
        self.assertRaises(ValueError, PolyOpts, max_exponential_value=None)
        self.assertRaises(ValueError, PolyOpts, variable_letters=None)


######################################################################################
class TestTerm(unittest.TestCase):
    def test_setting_values(self):
        term = Term(coefficient=-1, exponent=2)
        self.assertEqual(term.coefficient, -1)
        self.assertEqual(term.exponent, 2)

    def test_setting_values_exception(self):
        self.assertRaises(ValueError, Term, coefficient=1, exponent=None)
        self.assertRaises(ValueError, Term, coefficient=1, exponent=-1)
        self.assertRaises(ValueError, Term, coefficient=None, exponent=-1)

    def test_to_string(self):
        term = Term(coefficient=2, exponent=3)
        self.assertEqual(term.to_string("a"), "2a^3")
        term = Term(coefficient=-5, exponent=2)
        self.assertEqual(term.to_string("x"), "-5x^2")

    def test_to_string_unsigned(self):
        term = Term(coefficient=2, exponent=3)
        self.assertEqual(term.to_string_unsigned("a"), "2a^3")
        term = Term(coefficient=-5, exponent=2)
        self.assertEqual(term.to_string_unsigned("x"), "5x^2")

    def test_get_coefficient_sign(self):
        term = Term(coefficient=2, exponent=3)
        self.assertEqual(term.get_coefficient_sign(), NumberSign.POS)
        term = Term(coefficient=-5, exponent=2)
        self.assertEqual(term.get_coefficient_sign(), NumberSign.NEG)
        term = Term(coefficient=0, exponent=5)
        self.assertEqual(term.get_coefficient_sign(), NumberSign.ZERO)


#####################################################################################
class TestPolynomial(unittest.TestCase):
    def test_setting_values(self):
        polynomial = Polynomial(variable_letter="a")
        self.assertEqual(polynomial.variable_letter, "a")

    def test_setting_values_exceptions(self):
        self.assertRaises(ValueError, Polynomial, variable_letter=None)
        self.assertRaises(ValueError, Polynomial, variable_letter="")

    def test_add_term(self):
        term1 = Term(coefficient=2, exponent=5)
        term2 = Term(coefficient=-3, exponent=2)
        polynomial = Polynomial(variable_letter="x")
        self.assertListEqual(polynomial.terms, [])
        polynomial.add_term(term1)
        self.assertEqual(len(polynomial.terms), 1)
        self.assertEqual(polynomial.terms[0].to_string(polynomial.variable_letter), "2x^5")
        polynomial.add_term(term2)
        self.assertEqual(len(polynomial.terms), 2)
        self.assertEqual(polynomial.terms[1].to_string(polynomial.variable_letter), "-3x^2")

    def test_get_exponents(self):
        term1 = Term(coefficient=2, exponent=5)
        term2 = Term(coefficient=-3, exponent=2)
        term3 = Term(coefficient=-3, exponent=4)
        polynomial = Polynomial(variable_letter="x")
        self.assertListEqual(polynomial.get_exponents(), [])
        polynomial.add_term(term1)
        self.assertListEqual(polynomial.get_exponents(), [5])
        polynomial.add_term(term2)
        self.assertListEqual(polynomial.get_exponents(), [5, 2])
        polynomial.add_term(term3)
        self.assertListEqual(polynomial.get_exponents(), [5, 2, 4])

    def test_to_string(self):
        term1 = Term(coefficient=2, exponent=5)
        term2 = Term(coefficient=-3, exponent=2)
        term3 = Term(coefficient=+5, exponent=4)
        polynomial = Polynomial(variable_letter="x")
        polynomial.add_term(term1)
        polynomial.add_term(term2)
        polynomial.add_term(term3)
        self.assertEqual(polynomial.to_string(), "2x^5 - 3x^2 + 5x^4")

    def test_get_polynomial_order(self):
        term1 = Term(coefficient=2, exponent=1)
        term2 = Term(coefficient=-3, exponent=2)
        term3 = Term(coefficient=+5, exponent=4)
        polynomial = Polynomial(variable_letter="x")
        polynomial.add_term(term1)
        polynomial.add_term(term2)
        polynomial.add_term(term3)
        self.assertEqual(polynomial.get_polynomial_order(), PolynomialOrder.ASC)

        term1 = Term(coefficient=2, exponent=5)
        term2 = Term(coefficient=-3, exponent=3)
        term3 = Term(coefficient=+5, exponent=1)
        polynomial = Polynomial(variable_letter="x")
        polynomial.add_term(term1)
        polynomial.add_term(term2)
        polynomial.add_term(term3)
        self.assertEqual(polynomial.get_polynomial_order(), PolynomialOrder.DESC)

        term1 = Term(coefficient=2, exponent=5)
        term2 = Term(coefficient=-3, exponent=7)
        term3 = Term(coefficient=+5, exponent=1)
        polynomial = Polynomial(variable_letter="x")
        polynomial.add_term(term1)
        polynomial.add_term(term2)
        polynomial.add_term(term3)
        self.assertEqual(polynomial.get_polynomial_order(), PolynomialOrder.UNORDERED)


######################################################################################
class TestPolynomialOperations(unittest.TestCase):
    def test_generate_num_of_terms(self):
        polynomialOps = PolynomialOperations()
        # with at least one polynomial with 2 terms and one polinomial with 5 terms
        term_num_per_poly = polynomialOps.generate_num_of_terms(min_num_of_terms_in_poly=2, max_num_of_terms_in_poly=5,
                                                                num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertEqual(len(term_num_per_poly), 5)
        self.assertTrue(2 in term_num_per_poly)
        self.assertTrue(5 in term_num_per_poly)
        self.assertTrue(all(term_num >= 2 for term_num in term_num_per_poly))
        self.assertTrue(all(term_num <= 5 for term_num in term_num_per_poly))

    def test_generate_num_of_terms_exceptions(self):
        polynomialOps = PolynomialOperations()
        # None values
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=None,
                          max_num_of_terms_in_poly=5, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=None, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=5, num_of_polys=None, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=5, num_of_polys=5, term_num_per_poly=None)
        # negative value exception
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=-2,
                          max_num_of_terms_in_poly=5, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=-5, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=5, num_of_polys=-5, term_num_per_poly=[2, 5])
        # zero value exception
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=0,
                          max_num_of_terms_in_poly=5, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=0, num_of_polys=5, term_num_per_poly=[2, 5])
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=2,
                          max_num_of_terms_in_poly=5, num_of_polys=0, term_num_per_poly=[2, 5])
        # maximum value < minimum value exception
        self.assertRaises(ValueError, polynomialOps.generate_num_of_terms, min_num_of_terms_in_poly=5,
                          max_num_of_terms_in_poly=3, num_of_polys=5, term_num_per_poly=[2, 5])

    def test_generate_unique_numbers(self):
        polynomialOps = PolynomialOperations()
        # unique numbers
        unique_nums = polynomialOps.generate_unique_numbers(number_of_unique_numbers=3, min_value=1, max_value=3,
                                                            exclusions=[])
        unique_nums = sorted(unique_nums)
        self.assertEqual(len(unique_nums), 3)
        self.assertListEqual(unique_nums, [1, 2, 3])
        #unique numbers with exclusions
        unique_nums = polynomialOps.generate_unique_numbers(number_of_unique_numbers=3, min_value=1, max_value=5,
                                                            exclusions=[1, 3, 7])
        unique_nums = sorted(unique_nums)
        self.assertEqual(len(unique_nums), 3)
        self.assertListEqual(unique_nums, [2, 4, 5])

    def test_generate_unique_numbers_exceptions(self):
        polynomialOps = PolynomialOperations()
        # None values
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=None,
                          min_value=1, max_value=5, exclusions=[])
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=1,
                          min_value=None, max_value=5, exclusions=[])
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=1,
                          min_value=1, max_value=None, exclusions=[])
        # maximum value < minimum value exception
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=5,
                          min_value=5, max_value=3, exclusions=[])
        # not having enough unique values in an interval
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=5,
                          min_value=3, max_value=5, exclusions=[])
        # not having enough unique values in an interval because of exclusion
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=3,
                          min_value=3, max_value=5, exclusions=[3, 4])

    def test_generate_number(self):
        polynomialOps = PolynomialOperations()
        # random number
        generated_num = polynomialOps.generate_number(min_value=2, max_value=2, exclusions=[])
        self.assertEqual(generated_num, 2)
        # random number
        generated_num = polynomialOps.generate_number(min_value=2, max_value=5, exclusions=[])
        self.assertTrue(generated_num <= 5)
        self.assertTrue(2 <= generated_num)
        # random number with exclusions
        generated_num = polynomialOps.generate_number(min_value=2, max_value=5, exclusions=[2, 3, 5, 6])
        self.assertEqual(generated_num, 4)

    def test_generate_number_exceptions(self):
        polynomialOps = PolynomialOperations()
        # None values
        self.assertRaises(ValueError, polynomialOps.generate_number, min_value=None, max_value=2, exclusions=[])
        self.assertRaises(ValueError, polynomialOps.generate_number, min_value=2, max_value=None, exclusions=[])
        self.assertRaises(ValueError, polynomialOps.generate_number, min_value=2, max_value=2, exclusions=None)

        # maximum value < minimum value exception
        self.assertRaises(ValueError, polynomialOps.generate_number, min_value=5, max_value=3, exclusions=[])
        # not having any number in an interval because of exclusions
        self.assertRaises(ValueError, polynomialOps.generate_unique_numbers, number_of_unique_numbers=5,
                          min_value=3, max_value=5, exclusions=[3, 4, 5])

    def test_generate_polynomials(self):
        polyOpts = PolyOpts()
        polynomialOps = PolynomialOperations()
        polynomials = polynomialOps.generate_polynomials(polyOpts=polyOpts, number_of_polynomials=6)

        self.assertEqual(len(polynomials), 6)
        for polynomial in polynomials:
            # number of terms
            self.assertTrue(2 <= len(polynomial.terms) <= 4)
            # variable letter
            self.assertTrue(polynomial.variable_letter in ["x", "y", "z", "a", "b", "c"])
            for term in polynomial.terms:
                # coefficient
                self.assertTrue(-12 <= term.coefficient <= 12)
                # exponent
                self.assertTrue(1 <= term.exponent <= 5)
        # term number
        term_nums = [len(polynomial.terms) for polynomial in polynomials]
        self.assertTrue(2 in term_nums)
        self.assertTrue(4 in term_nums)