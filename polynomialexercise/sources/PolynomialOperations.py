import random
from random import randint, shuffle
from enum import Enum, auto


def _check_if_params_none(params):
    """
    Checks if any of the parameters is None.

    Params
    ------
    params : list
        list of parameters

    Returns
    -------
    result : bool
        True if any of the paramter is None, False otherwise
    """
    return True if any(param is None for param in params) else False


def _check_if_params_smaller_or_greater_than_a_value(params, value, operation="lt", type="all"):
    """
    Checks if all of the parameters are greater than, greater than or equal, less than, less than or equal.

    Params
    ------
    params : list
        list of parameters
    value : int
        value to compare parameter values
    operation : str (default is lt)
        comparison operation (lt: less than, lte: less than or equal, gt: greater than, gte: greater than or equal)
    type : str (default is all)
        if all of the parameters or any of the parameter should satisfy the requirement (options: all, any)

    Returns
    -------
    result : bool
        True if all of the parameters satisfies the requirement, False otherwise
    """
    if operation == "lt":
        if type == "all":
            return True if all(param < value for param in params) else False
        else:
            return True if any(param < value for param in params) else False
    elif operation == "lte":
        if type == "all":
            return True if all(param <= value for param in params) else False
        else:
            return True if any(param <= value for param in params) else False
    elif operation == "gt":
        if type == "all":
            return True if all(param > value for param in params) else False
        else:
            return True if any(param > value for param in params) else False
    elif operation == "gte":
        if type == "all":
            return True if all(param >= value for param in params) else False
        else:
            return True if any(param >= value for param in params) else False
    else:
        raise ValueError("operation must be one of the followings: lt, lte, gt, gte!")


class NumberSign(Enum):
    """
    Enum class to store possible signs (negative, positive, and zero) of integers.
    """
    NEG = auto()
    POS = auto()
    ZERO = auto()


class PolynomialOrder(Enum):
    """
    Enum class to store possible ordering (ascending, descending, and unordered) of an list of numbers. Both ascending
    and descending order at the same time (e.g., [2, 2, 2]) is not included since it is not needed in the scope of the
    project.
    """
    ASC = auto()
    DESC = auto()
    UNORDERED = auto()


class RandomNumberGenerator:
    def __init__(self, seed=None):
        self.seed = seed

    def generate_random_number(self, min_value, max_value):
        """
        Generates random number between given interval.

        Parameters
        ----------
        min_value : int
            minimum value to be generated
        max_value : int
            maximum value to be generated

        Returns
        -------
        random_number : int
            randomly generated number
        """
        if _check_if_params_none([min_value, max_value]):
            raise ValueError("parameters cannot be None!")
        if max_value < max_value:
            raise ValueError("max_value cannot be smaller than min_value!")
        random.seed(self.seed)
        return randint(min_value, max_value)


class PolyOpts:
    """
    Class to define and store the options of polynomials to generate them randomly.
    """
    def __init__(self, min_num_of_terms_in_poly=2, max_num_of_terms_in_poly=4, term_num_per_poly = [2, 4],
                 min_coefficient_value = -12, max_coefficient_value = 12, min_exponential_value = 1,
                 max_exponential_value = 5, variable_letters = ["x", "y", "z", "a", "b", "c"]):
        """
        Initialize the parameters of the polynomials.

        Parameters
        ----------
        min_num_of_terms_in_poly : int
            minimum number of terms that a polynomial can include (the default is 2)
        max_num_of_terms_in_poly : int
            maximum number of terms that a polynomial can include (the default is)
        term_num_per_poly : list
            list of the numbers of terms of the polynomials (the default is [2, 4])
        min_coefficient_value : int
            minimum coefficient value (the default is -12)
        max_coefficient_value : int
            maximum coefficient value (the default is 12)
        min_exponential_value : int
            minimum exponent value (the default is 1)
        max_exponential_value : int
            maximum exponent value (the default is 5)
        variable_letters : list
            list of variable letters (the default is ["x", "y", "z", "a", "b", "c"])
        """

        if _check_if_params_none([min_num_of_terms_in_poly, max_num_of_terms_in_poly, term_num_per_poly,
                                  min_coefficient_value, max_coefficient_value, min_exponential_value,
                                  max_exponential_value, variable_letters]):
            raise ValueError("parameters cannot be None!")
        if _check_if_params_smaller_or_greater_than_a_value([min_num_of_terms_in_poly, max_num_of_terms_in_poly], 1, "lt", type="any"):
            raise ValueError("min_num_of_terms_in_poly and max_num_of_terms_in_poly cannot be smaller than 1!")
        if max_num_of_terms_in_poly < min_num_of_terms_in_poly:
            raise ValueError("max_num_of_terms_in_poly cannot be smaller than min_num_of_terms_in_poly!")
        if max_coefficient_value < min_coefficient_value:
            raise ValueError("max_coefficient_value cannot be smaller than min_coefficient_value!")
        if _check_if_params_smaller_or_greater_than_a_value([min_exponential_value, max_exponential_value], 0, "lt", type="any"):
            raise ValueError("min_exponential_value and max_exponential_value cannot be negative!")
        if max_exponential_value < min_exponential_value:
            raise ValueError("max_exponential_value cannot be smaller than max_exponential_value!")

        self.min_num_of_terms_in_poly = min_num_of_terms_in_poly
        self.max_num_of_terms_in_poly = max_num_of_terms_in_poly
        self.term_num_per_poly = term_num_per_poly
        self.min_coefficient_value = min_coefficient_value
        self.max_coefficient_value = max_coefficient_value
        self.min_exponential_value = min_exponential_value
        self.max_exponential_value = max_exponential_value
        self.variable_letters = variable_letters

# todo:check default term_num_per_poly with min max values


class Term:
    """
    Class to store the coefficient and exponent values of the term.
    """
    def __init__(self, coefficient, exponent):
        """
        Initialize the attributes of the term.

        Parameters
        ----------
        coefficient : int
            coefficient value of the term
        exponent : int
            exponent value of the term
        """
        if _check_if_params_none([coefficient, exponent]):
            raise ValueError("coefficient and exponent cannot be None!")
        if _check_if_params_smaller_or_greater_than_a_value([exponent], 0, "lt", type="any"):
            raise ValueError("exponent cannot be negative!")
        self.coefficient = coefficient
        self.exponent = exponent

    def to_string(self, variable_letter):
        """
        Returns the string representation of the term. Includes "-" if the term is negative.

        Parameters
        ----------
        variable_letter : char
            the variable letter to be used in the polynomial

        Returns
        -------
        term_str : str
            string representation of the term
        """
        return "{}{}^{}".format(self.coefficient, variable_letter, self.exponent)

    def to_string_unsigned(self, variable_letter):
        """
        Returns the unsigned string representation of the term. The sign of the coefficient is discarded.

        Parameters
        ----------

        variable_letter : char
            the variable letter to be used in the polynomial

        Returns
        -------
        term_str : str
            string representation of the unsigned term
        """
        return "{}{}^{}".format(abs(self.coefficient), variable_letter, self.exponent)

    def get_coefficient_sign(self):
        """
        Returns the sign of the term.

        Returns
        -------
        term_sign : enum value of NumberSign class (NumberSign.NEG, NumberSign.POS, NumberSign.ZERO)
            the sign of the term
        """
        return NumberSign.NEG if self.coefficient<0 else NumberSign.POS if self.coefficient>0 else NumberSign.ZERO


class Polynomial:
    """
    Class to store the terms of the polynomial.
    """
    def __init__(self, variable_letter):
        """
        Initialize the attributes of the polynomials.

        Parameters
        ----------
        variable_letter: char
            variable letter to represent variable of the polynomial.
        """
        if _check_if_params_none([variable_letter]):
            raise ValueError("variable_letter cannot be None!")
        if not variable_letter:
            raise ValueError("variable_letter cannot be empty!")
        self.variable_letter = variable_letter
        self.terms = []

    def add_term(self, term):
        """
        Add a term to the polynomial.

        Parameters
        ----------
        term: Term
            Term object to add to the polynomial

        Returns
        -------
        None
        """
        self.terms.append(term)

    def get_exponents(self):
        """
        Returns the exponent values of the polynomial in adding order.

        Returns
        -------
        exponents : list
            list of the exponents of the polynomial
        """
        return [term.exponent for term in self.terms]

    def to_string(self):
        """
        Returns the string representation of the polynomial.

        Returns
        -------
        polynomial_str : str
            string representation of the polynomial
        """
        polynomial_str = ""
        for index, term in enumerate(self.terms):
            if index==0:
                polynomial_str += "-" if term.get_coefficient_sign()==NumberSign.NEG else ""
                polynomial_str += term.to_string_unsigned(self.variable_letter)
            else:
                polynomial_str += " - " if term.get_coefficient_sign()==NumberSign.NEG else " + "
                polynomial_str += term.to_string_unsigned(self.variable_letter)
        return polynomial_str

    def get_polynomial_order(self):
        """
        Returns if the exponents of the polynomial are ordered in descending or ascending order, or if they are unordered.

        Returns
        -------
        polynomial_order : enum value of NumberSign class (PolynomialOrder.ASC, PolynomialOrder.DESC, PolynomialOrder.UNORDERED)
            the order type of the polynomial
        """
        polynomial_order = PolynomialOrder.ASC
        exponents = self.get_exponents()
        if len(exponents)<2:
            return polynomial_order
        if exponents[1] < exponents[0]:
            polynomial_order = PolynomialOrder.DESC
        for index in range(1, len(exponents)-1):
            if (polynomial_order is PolynomialOrder.ASC and exponents[index] > exponents[index+1]) or\
                    (polynomial_order is PolynomialOrder.DESC and exponents[index] < exponents[index+1]):
                return PolynomialOrder.UNORDERED
        return polynomial_order


class PolynomialOperations:
    """
    Includes the operations to generate polynomials according to the given requirements.
    """
    def __init__(self, random_number_generator=RandomNumberGenerator()):
        self.random_number_generator = random_number_generator

    def generate_num_of_terms(self, min_num_of_terms_in_poly, max_num_of_terms_in_poly, num_of_polys,
                              term_num_per_poly=[2, 4]):
        """
        Randomly generated how many terms the polynomials will include.

        Parameters
        ----------
        min_num_of_terms_in_poly : int
            minimum number of terms that a polynomial can include
        max_num_of_terms_in_poly : int
            maximum number of terms that a polynomial can include
        num_of_polys : int
            number of polynomials to generate
        term_num_per_poly : list
            list of the numbers of terms of the polynomials

        Returns
        -------
        term_num_per_poly : list
            list of the number of terms per polynomial

        """
        if _check_if_params_none([min_num_of_terms_in_poly, max_num_of_terms_in_poly, num_of_polys, term_num_per_poly]):
            raise ValueError("parameters cannot be None!")
        if _check_if_params_smaller_or_greater_than_a_value([min_num_of_terms_in_poly,
                                                             max_num_of_terms_in_poly, num_of_polys], 1, "lt", type="any"):
            raise ValueError("parameters must be greater than zero!")
        if min_num_of_terms_in_poly > max_num_of_terms_in_poly:
            raise ValueError("Minimum element must be less than maximum element!")

        while len(term_num_per_poly)<num_of_polys:
            term_num_per_poly.append(self.random_number_generator.generate_random_number
                                     (min_num_of_terms_in_poly, max_num_of_terms_in_poly))
        shuffle(term_num_per_poly)
        return term_num_per_poly

    def generate_unique_numbers(self, number_of_unique_numbers, min_value, max_value, exclusions=[]):
        """
        Generates non-duplicate numbers between an interval.

        Parameters
        ----------
        number_of_unique_numbers : int
            how many numbers to randomly generate
        min_value : int
            minimum value that can be generated
        max_value : int
            maximum value that can be generated
        exclusions : list
            the values that must be excluded during the random generation of numbers

        Returns
        -------
        random_value : list
            list of randomly generated numbers
        """

        if _check_if_params_none([number_of_unique_numbers, min_value, max_value]):
            raise ValueError("parameters cannot be None!")
        if min_value > max_value:
            raise ValueError("Minimum value must be less than maximum value!")
        exclusions_in_interval = [True if ((elem <= max_value) and (elem >= min_value)) else False for elem in exclusions]
        if not (((max_value-min_value)+1)-sum(exclusions_in_interval) >= number_of_unique_numbers):
            raise ValueError("There is not {} unique values between {} and {}".format(number_of_unique_numbers,
                                                                                      min_value, max_value))

        unique_numbers = []
        while len(unique_numbers) < number_of_unique_numbers:
            random_value = self.generate_number(min_value=min_value, max_value=max_value, exclusions=exclusions)
            if random_value in unique_numbers:
                continue
            unique_numbers.append(random_value)
        return unique_numbers

    def generate_number(self, min_value, max_value, exclusions=[]):
        """
        Randomly generates a number between an interval.
        min_value : int
            minimum value that can be generated
        max_value : int
            maximum value that can be generated
        exclusions : int
            the values that must be excluded during the random generation of numbers

        Returns
        -------
        random_value : int
            Randomly generated number
        """
        if _check_if_params_none([min_value, max_value, exclusions]):
            raise ValueError("parameters cannot be None!")
        if min_value > max_value:
            raise ValueError("Minimum value must be less than maximum value!")
        exclusions_in_interval = [True if ((elem <= max_value) and (elem >= min_value)) else False for elem in exclusions]
        if not (((max_value - min_value) + 1) - sum(exclusions_in_interval) >= 1):
            raise ValueError("There is no number between {} and {} when we exclude the numbers {}".
                             format(min_value, max_value, exclusions))

        random_value = self.random_number_generator.generate_random_number(min_value, max_value)
        while random_value in exclusions:
            random_value = self.random_number_generator.generate_random_number(min_value, max_value)
        return random_value

    def generate_polynomials(self, polyOpts, number_of_polynomials):
        """
        Generates polynomial based on the given requirements.

        Parameters
        ----------
        polyOpts : PolyOpts
             PolyOpts object that includes the requirements to generate polynomials
        number_of_polynomials : int
            number of polynomials to generate

        Returns
        -------
        polynomials : list
            list of polynomials
        """
        number_of_terms = self.generate_num_of_terms(min_num_of_terms_in_poly=polyOpts.min_num_of_terms_in_poly,
                                                     max_num_of_terms_in_poly=polyOpts.max_num_of_terms_in_poly,
                                                     num_of_polys=number_of_polynomials)
        polynomials = []
        for number_of_term in number_of_terms:
            variable_letter = polyOpts.variable_letters[self.generate_number(min_value=0, max_value=len(polyOpts.variable_letters)-1)]
            poly = Polynomial(variable_letter=variable_letter)
            exponents = self.generate_unique_numbers(number_of_unique_numbers=number_of_term,
                                                     min_value=polyOpts.min_exponential_value,
                                                     max_value=polyOpts.max_exponential_value)
            for exponent in exponents:
                coefficient = self.generate_number(min_value=polyOpts.min_coefficient_value,
                                                   max_value=polyOpts.max_coefficient_value,
                                                   exclusions=[0])
                poly.add_term(Term(coefficient=coefficient, exponent=exponent))
            polynomials.append(poly)
        return polynomials
