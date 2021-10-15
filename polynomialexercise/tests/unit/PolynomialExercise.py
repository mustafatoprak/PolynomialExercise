import io
import unittest
from unittest.mock import patch
# from ...sources.PolynomialOperations import Term, Polynomial
# from ...sources.PolynomialExercise import PolynomialExercise
from polynomialexercise.sources.PolynomialOperations import Term, Polynomial
from polynomialexercise.sources.PolynomialExercise import PolynomialExercise


######################################################################################
class TestPolynomialExercise(unittest.TestCase):
    def setUp(self):
        # creating PolynomialExercise object
        self.polynomial_exercise = PolynomialExercise()

        # exercise 1 with all ascending, descending, and unordered polynomials
        # polynomial1
        poly1 = Polynomial(variable_letter="x")
        poly1.add_term(Term(2, 2))
        poly1.add_term(Term(-2, 3))
        poly1.add_term(Term(5, 5))
        # polynomial2
        poly2 = Polynomial(variable_letter="y")
        poly2.add_term(Term(3, 7))
        poly2.add_term(Term(5, 5))
        poly2.add_term(Term(-4, 2))
        # polynomial3
        poly3 = Polynomial(variable_letter="z")
        poly3.add_term(Term(-1, 5))
        poly3.add_term(Term(4, 3))
        poly3.add_term(Term(4, 5))
        self.exercise_all = {"A": poly1, "B": poly2, "C": poly3}
        self.exercise_no_asc_poly = {"B": poly2, "C": poly3}
        self.exercise_no_desc_poly = {"A": poly1, "C": poly3}
        self.exercise_no_unordered_poly = {"A": poly1, "B": poly2}
        self.exercise_no_ordered_poly = {"A": poly3}

    def test___get_polynomial_orders(self):
        # extracting polynomial orders
        ascending_polynomials, descending_polynomials, unordered_polynomials = \
            self.polynomial_exercise._PolynomialExercise__get_polynomial_orders(self.exercise_all)
        self.assertListEqual(list(ascending_polynomials.keys()), ["A"])
        self.assertListEqual(list(descending_polynomials.keys()), ["B"])
        self.assertListEqual(list(unordered_polynomials.keys()), ["C"])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, method, exercise, expected_output, mock_stdout):
        method(exercise)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_generate_delivery(self):
        # with ordered polynomials
        expected_output_result = "\nConsegna:\n\tSeleziona i polinomi ordinati:\n\tA, B\n\n"
        method = self.polynomial_exercise.generate_delivery
        self.assert_stdout(method, self.exercise_all, expected_output_result)

        # with no ordered polynomials
        expected_output_result = "\nConsegna:\n\tSeleziona i polinomi ordinati:\n\t- non c'è polinomio ordinato tra le opzioni!\n\n"
        method = self.polynomial_exercise.generate_delivery
        self.assert_stdout(method, self.exercise_no_ordered_poly, expected_output_result)

    def test_generate_response_options(self):
        expected_output_result = "Opzioni di risposta:\n[A] 2x^2 - 2x^3 + 5x^5\n[B] 3y^7 + 5y^5 - 4y^2\n[C] -1z^5 + 4z^3 + 4z^5\n"
        method = self.polynomial_exercise.generate_response_options
        self.assert_stdout(method, self.exercise_all, expected_output_result)

    def test_generate_guided_solution_all(self):
        expected_output_result = "\nRisoluzione guidata:" +\
                                 "\n\t1. I polinomi non ordinati" +\
                                 "\n\tUn polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati " \
                                 "secondo le potenze crescenti (o decrescenti) di quella lettera:" +\
                                 "\n\tdevi escludere i polinomi in cui gli esponenti " \
                                 "non sono in ordine crescente o decrescente." + "\n\t[C] -1z^5 + 4z^3 + 4z^5" +\
                                 "\n\n\t2. I polinomi ordinati secondo le potenze crescenti:" + "\n\t\t[A] 2x^2 - 2x^3 + 5x^5" +\
                                 "\n\t   I polinomi ordinati secondo le potenze decrescenti:" + "\n\t\t[B] 3y^7 + 5y^5 - 4y^2\n"
        method = self.polynomial_exercise.generate_guided_solution
        self.assert_stdout(method, self.exercise_all, expected_output_result)

    def test_generate_guided_solution_no_asc_poly(self):
        expected_output_result = "\nRisoluzione guidata:" + \
                                 "\n\t1. I polinomi non ordinati" + \
                                 "\n\tUn polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati " \
                                 "secondo le potenze crescenti (o decrescenti) di quella lettera:" + \
                                 "\n\tdevi escludere i polinomi in cui gli esponenti " \
                                 "non sono in ordine crescente o decrescente." + "\n\t[C] -1z^5 + 4z^3 + 4z^5" + \
                                 "\n\n\t2. I polinomi ordinati secondo le potenze crescenti:" + "\n\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!" + \
                                 "\n\t   I polinomi ordinati secondo le potenze decrescenti:" + "\n\t\t[B] 3y^7 + 5y^5 - 4y^2\n"
        method = self.polynomial_exercise.generate_guided_solution
        self.assert_stdout(method, self.exercise_no_asc_poly, expected_output_result)

    def test_generate_guided_solution_no_desc_poly(self):
        expected_output_result = "\nRisoluzione guidata:" +\
                                 "\n\t1. I polinomi non ordinati" +\
                                 "\n\tUn polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati " \
                                 "secondo le potenze crescenti (o decrescenti) di quella lettera:" +\
                                 "\n\tdevi escludere i polinomi in cui gli esponenti " \
                                 "non sono in ordine crescente o decrescente." + "\n\t[C] -1z^5 + 4z^3 + 4z^5" +\
                                 "\n\n\t2. I polinomi ordinati secondo le potenze crescenti:" + "\n\t\t[A] 2x^2 - 2x^3 + 5x^5" +\
                                 "\n\t   I polinomi ordinati secondo le potenze decrescenti:" + "\n\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!\n"
        method = self.polynomial_exercise.generate_guided_solution
        self.assert_stdout(method, self.exercise_no_desc_poly, expected_output_result)

    def test_generate_guided_solution_no_unordered_poly(self):
        expected_output_result = "\nRisoluzione guidata:" + \
                                 "\n\t1. I polinomi non ordinati" + \
                                 "\n\tUn polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati " \
                                 "secondo le potenze crescenti (o decrescenti) di quella lettera:" + \
                                 "\n\tdevi escludere i polinomi in cui gli esponenti " \
                                 "non sono in ordine crescente o decrescente." + "\n\t\t- non c'è polinomio non ordinato tra le opzioni!" + \
                                 "\n\n\t2. I polinomi ordinati secondo le potenze crescenti:" + "\n\t\t[A] 2x^2 - 2x^3 + 5x^5" + \
                                 "\n\t   I polinomi ordinati secondo le potenze decrescenti:" + "\n\t\t[B] 3y^7 + 5y^5 - 4y^2\n"
        method = self.polynomial_exercise.generate_guided_solution
        self.assert_stdout(method, self.exercise_no_unordered_poly, expected_output_result)










    def test_generate_correct_response(self):
        expected_output_result = "\nOpzioni di risposto:" + "\n\tcorrette:" +\
                                 "\n\t\t- [A] polinomio ordinato crescente: [A] con termini nA = 3" +\
                                 "\n\t\t- [B] polinomio ordinato decrescente: [B] con termini nB = 3" +\
                                 "\n\tsbagliate:" +\
                                 "\n\t\t- [C] polinomio non ordinato \n"

        method = self.polynomial_exercise.generate_correct_response
        self.assert_stdout(method, self.exercise_all, expected_output_result)

    def test_generate_correct_response_no_asc_poly(self):
        expected_output_result = "\nOpzioni di risposto:" + "\n\tcorrette:" + \
                                 "\n\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!" + \
                                 "\n\t\t- [B] polinomio ordinato decrescente: [B] con termini nB = 3" + \
                                 "\n\tsbagliate:" + \
                                 "\n\t\t- [C] polinomio non ordinato \n"
        method = self.polynomial_exercise.generate_correct_response
        self.assert_stdout(method, self.exercise_no_asc_poly, expected_output_result)

    def test_generate_correct_response_no_desc_poly(self):
        expected_output_result = "\nOpzioni di risposto:" + "\n\tcorrette:" + \
                                 "\n\t\t- [A] polinomio ordinato crescente: [A] con termini nA = 3" + \
                                 "\n\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!" + \
                                 "\n\tsbagliate:" + \
                                 "\n\t\t- [C] polinomio non ordinato \n"
        method = self.polynomial_exercise.generate_correct_response
        self.assert_stdout(method, self.exercise_no_desc_poly, expected_output_result)

    def test_generate_correct_response_no_unordered_poly(self):
        expected_output_result = "\nOpzioni di risposto:" + "\n\tcorrette:" + \
                                 "\n\t\t- [A] polinomio ordinato crescente: [A] con termini nA = 3" + \
                                 "\n\t\t- [B] polinomio ordinato decrescente: [B] con termini nB = 3" + \
                                 "\n\tsbagliate:" + \
                                 "\n\t\t- non c'è polinomio non ordinato tra le opzioni!\n"
        method = self.polynomial_exercise.generate_correct_response
        self.assert_stdout(method, self.exercise_no_unordered_poly, expected_output_result)
