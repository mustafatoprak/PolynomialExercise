from abc import ABC, abstractmethod
from collections import defaultdict
from polynomialexercise.sources.PolynomialOperations import PolynomialOrder, PolynomialOperations, PolyOpts


class AbstractPolynomialExercise(ABC):
    """
    Abstract class to guarantee to have required functions (generate_delivery, generate_response_options,
    generate_guided_solution, generate_correct_response) to be implemented for creating a complete exercise.
    """
    def __init__(self):
        super().__init__()


    @abstractmethod
    def generate_delivery(self, exercise):
        pass

    @abstractmethod
    def generate_response_options(self, exercise):
        pass

    @abstractmethod
    def generate_guided_solution(self, exercise):
        pass

    @abstractmethod
    def generate_correct_response(self, exercise):
        pass

    @abstractmethod
    def generate_exercise(self, number_of_polynomials, options_letters, polyOpts):
        pass


class PolynomialExercise(AbstractPolynomialExercise):
    """
    A concrete class, which inherits AbstractPolynomialExercise, including the implementation of required classes
    (generate_delivery, generate_response_options, generate_guided_solution, generate_correct_response).
    """
    def __get_polynomial_orders(self, exercise):
        """
        Extracts the orders of the polynomials. If there is no polynomial in a specific ordering, an empty list is
        returned.

        Params
        ------
        exercise : dict
            dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})

        Returns
        -------
        ascending_polynomials : list
            list of ascending ordered polynomials
        descending_polynomials : list
            list of descending ordered polynomials
        unordered_polynomials : list
            list of unordered polynomials
        """

        ascending_polynomials = {option:polynomial for option, polynomial in exercise.items()
                                 if polynomial.get_polynomial_order() == PolynomialOrder.ASC}
        descending_polynomials = {option:polynomial for option, polynomial in exercise.items()
                                  if polynomial.get_polynomial_order() == PolynomialOrder.DESC}
        unordered_polynomials = {option:polynomial for option, polynomial in exercise.items()
                                 if polynomial.get_polynomial_order() == PolynomialOrder.UNORDERED}
        return ascending_polynomials, descending_polynomials, unordered_polynomials

    def generate_delivery(self, exercise):
        """
        Generates the delivery section of the exercise.

        Parameters
        ----------
        exercise : dict
            dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})

        Returns
        -------
        None
        """
        output_str = "\nConsegna:" +\
                     "\n\tSeleziona i polinomi ordinati:" +\
                     "\n\t{}\n"
        ascending_polynomials, descending_polynomials, _ = self.__get_polynomial_orders(exercise)
        delivery = list(ascending_polynomials.keys()) + list(descending_polynomials.keys())
        # delivery = [option for option, polynomial in self.exercise.items()
        #             if polynomial.get_polynomial_order() in [PolynomialOrder.ASC, PolynomialOrder.DESC]]
        if len(delivery)>0:
            delivery.sort()
            result_str = output_str.format(", ".join(delivery))
        else:
            result_str = output_str.format("- non c'è polinomio ordinato tra le opzioni!")
        print(result_str)

    def generate_response_options(self, exercise):
        """
        Generates the response option section of the exercise.

        Parameters
        ----------
        exercise : dict
            dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})

        Returns
        -------
        None
        """
        exercise_options = ["[{}] {}".format(option, polynomial.to_string())
                            for option, polynomial in exercise.items()]
        output_str = "Opzioni di risposta:\n{}".format("\n".join(exercise_options))
        print(output_str)

    def generate_guided_solution(self, exercise):
        """
        Generates the guided solution section of the exercise.

        Parameters
        ----------
        exercise : dict
            dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})

        Returns
        -------
        None
        """
        ascending_polynomials, descending_polynomials, unordered_polynomials = self.__get_polynomial_orders(exercise)

        output_str = "\nRisoluzione guidata:" +\
                     "\n\t1. I polinomi non ordinati" +\
                     "\n\tUn polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le " \
                     "potenze crescenti (o decrescenti) di quella lettera:" +\
                     "\n\tdevi escludere i polinomi in cui gli esponenti " \
                     "non sono in ordine crescente o decrescente." + "\n{}" +\
                     "\n\n\t2. I polinomi ordinati secondo le potenze crescenti:" + "\n{}" +\
                     "\n\t   I polinomi ordinati secondo le potenze decrescenti:" + "\n{}"

        if len(unordered_polynomials)>0:
            unordered_out_str = ["\t[{}] {}".format(option, polynomial.to_string())
                                          for option, polynomial in unordered_polynomials.items()]
            unordered_out_str = "\n".join(unordered_out_str)
        else:
            unordered_out_str = "\t\t- non c'è polinomio non ordinato tra le opzioni!"
        if len(ascending_polynomials)>0:
            ascending_out_str = ["\t\t[{}] {}".format(option, polynomial.to_string())
                                         for option, polynomial in ascending_polynomials.items()]
            ascending_out_str = "\n".join(ascending_out_str)
        else:
            ascending_out_str = "\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!"
        if len(descending_polynomials)>0:
            descending_out_str = ["\t\t[{}] {}".format(option, polynomial.to_string())
                                      for option, polynomial in descending_polynomials.items()]
            descending_out_str = "\n".join(descending_out_str)
        else:
            descending_out_str = "\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!"

        output_str = output_str.format(unordered_out_str, ascending_out_str, descending_out_str)
        print(output_str)


    # def generate_correct_response(self, exercise):
    #     """
    #     Generates the correct response section of the exercise.
    #
    #     Parameters
    #     ----------
    #     exercise : dict
    #         dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})
    #
    #     Returns
    #     -------
    #     None
    #     """
    #     def group_dict_keys_by_values(dictionary):
    #         grouped_list = defaultdict(list)
    #         for key, value in sorted(dictionary.items()):
    #             grouped_list[value].append(key)
    #         return grouped_list
    #
    #     ascending_polynomials, descending_polynomials, unordered_polynomials = self.__get_polynomial_orders(exercise)
    #
    #     print("\nOpzioni di risposto:")
    #     print("\tcorrette:")
    #     if len(ascending_polynomials) > 0:
    #         number_of_terms = {option:len(polynomial.terms) for option, polynomial in ascending_polynomials.items()}
    #         number_of_terms = group_dict_keys_by_values(number_of_terms)
    #         ascending_polynomials_str = ", ".join(["[{}]".format(option) for option, polynomial in ascending_polynomials.items()])
    #         ascending_polynomials_str += " polinomi ordinati crescenti:" if len(ascending_polynomials)>0 else " polinomio ordinato crescente,"
    #
    #         num_of_term_strs = []
    #         for num_of_term, options in number_of_terms.items():
    #             opts = " ".join(["[{}]".format(option) for option in options])
    #             terms = " = ".join(["n{}".format(option) for option in options])
    #             num_of_term_strs.append(opts + " con termini " + terms + " = {}".format(num_of_term))
    #         ascending_polynomials_str += ", ".join(num_of_term_strs)
    #         print("\t\t- " + ascending_polynomials_str)
    #     else:
    #         print("\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!")
    #     # print("   I polinomi ordinati secondo le potenze decrescenti:")
    #     if len(descending_polynomials) > 0:
    #         number_of_terms = {option: len(polynomial.terms) for option, polynomial in descending_polynomials.items()}
    #         number_of_terms = group_dict_keys_by_values(number_of_terms)
    #         descending_polynomials_str = ", ".join(
    #             ["[{}]".format(option) for option, polynomial in descending_polynomials.items()])
    #         descending_polynomials_str += " polinomi ordinati decrescenti:" if len(
    #             descending_polynomials) > 0 else " polinomio ordinato decrescente,"
    #
    #         num_of_term_strs = []
    #         for num_of_term, options in number_of_terms.items():
    #             opts = " ".join(["[{}]".format(option) for option in options])
    #             terms = " = ".join(["n{}".format(option) for option in options])
    #             num_of_term_strs.append(opts + " con termini " + terms + " = {}".format(num_of_term))
    #         descending_polynomials_str += ", ".join(num_of_term_strs)
    #         print("\t\t- " + descending_polynomials_str)
    #     else:
    #         print("\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!")
    #     print("\tsbagliate:")
    #     if len(unordered_polynomials) > 0:
    #         unordered_polynomials_str = " ".join(["[{}]".format(option, polynomial.to_string())
    #                                               for option, polynomial in unordered_polynomials.items()])
    #         unordered_polynomials_str += " polinomi non ordinati" if len(
    #             ascending_polynomials) > 0 else " polinomio non ordinato"
    #         print("\t\t- {} ".format(unordered_polynomials_str))
    #     else:
    #         print("\t\t- non c'è polinomio non ordinato tra le opzioni!")

    def generate_correct_response(self, exercise):
        """
        Generates the correct response section of the exercise.

        Parameters
        ----------
        exercise : dict
            dictionary of option-polynomial match (e.g. {A: Polynomial1, B: Polynomial2})

        Returns
        -------
        None
        """
        def group_dict_keys_by_values(dictionary):
            grouped_list = defaultdict(list)
            for key, value in sorted(dictionary.items()):
                grouped_list[value].append(key)
            return grouped_list

        ascending_polynomials, descending_polynomials, unordered_polynomials = self.__get_polynomial_orders(exercise)

        output_str = "\nOpzioni di risposto:" + "\n\tcorrette:" + "\n{}" + "\n{}" + "\n\tsbagliate:" + "\n{}"
        if len(ascending_polynomials) > 0:
            number_of_terms = {option:len(polynomial.terms) for option, polynomial in ascending_polynomials.items()}
            number_of_terms = group_dict_keys_by_values(number_of_terms)
            ascending_polynomials_str = ", ".join(["[{}]".format(option) for option, polynomial in ascending_polynomials.items()])
            ascending_polynomials_str += " polinomi ordinati crescenti: " if len(ascending_polynomials)>1 else " polinomio ordinato crescente: "

            num_of_term_strs = []
            for num_of_term, options in number_of_terms.items():
                opts = " ".join(["[{}]".format(option) for option in options])
                terms = " = ".join(["n{}".format(option) for option in options])
                num_of_term_strs.append(opts + " con termini " + terms + " = {}".format(num_of_term))
            ascending_polynomials_str += ", ".join(num_of_term_strs)
            ascending_polynomials_str = "\t\t- " + ascending_polynomials_str
        else:
            ascending_polynomials_str = "\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!"
        # print("   I polinomi ordinati secondo le potenze decrescenti:")
        if len(descending_polynomials) > 0:
            number_of_terms = {option: len(polynomial.terms) for option, polynomial in descending_polynomials.items()}
            number_of_terms = group_dict_keys_by_values(number_of_terms)
            descending_polynomials_str = ", ".join(
                ["[{}]".format(option) for option, polynomial in descending_polynomials.items()])
            descending_polynomials_str += " polinomi ordinati decrescenti: " if len(
                descending_polynomials) > 1 else " polinomio ordinato decrescente: "

            num_of_term_strs = []
            for num_of_term, options in number_of_terms.items():
                opts = " ".join(["[{}]".format(option) for option in options])
                terms = " = ".join(["n{}".format(option) for option in options])
                num_of_term_strs.append(opts + " con termini " + terms + " = {}".format(num_of_term))
            descending_polynomials_str += ", ".join(num_of_term_strs)
            descending_polynomials_str = "\t\t- " + descending_polynomials_str
        else:
            descending_polynomials_str = "\t\t- non c'è polinomio ordinato secondo le potenze crescenti tra le opzioni!"
        if len(unordered_polynomials) > 0:
            unordered_polynomials_str = " ".join(["[{}]".format(option, polynomial.to_string())
                                                  for option, polynomial in unordered_polynomials.items()])
            unordered_polynomials_str += " polinomi non ordinati" if len(
                ascending_polynomials) > 1 else " polinomio non ordinato"
            unordered_polynomials_str = "\t\t- {} ".format(unordered_polynomials_str)
        else:
            unordered_polynomials_str = "\t\t- non c'è polinomio non ordinato tra le opzioni!"
        a = output_str.format(ascending_polynomials_str, descending_polynomials_str, unordered_polynomials_str)
        print(a)

    def generate_exercise(self, number_of_polynomials, options_letters, polyOpts = PolyOpts()):
        """
        Generates the exercise including the sections: consegna, opzioni di risposto, risoluzione guidata, and
        risposta corretta.

        Parameters
        ----------
        number_of_polynomials : int
            number of polynomials to be generated
        options_letters : list
            list of variable letters to be used in the polynomials
        polyOpts : PolyOpts
            options/requirements to generate random polynomials

        Returns
        -------
        None
        """
        polynomial_operations = PolynomialOperations()
        polynomials = polynomial_operations.generate_polynomials(polyOpts=polyOpts,
                                                                 number_of_polynomials=number_of_polynomials)
        polynomials = polynomials
        exercise = {options_letters[i]: polynomials[i] for i in range(len(polynomials))}
        self.generate_delivery(exercise)
        self.generate_response_options(exercise)
        self.generate_guided_solution(exercise)
        self.generate_correct_response(exercise)
