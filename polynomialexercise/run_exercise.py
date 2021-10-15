from polynomialexercise.sources.PolynomialExercise import PolynomialExercise

import sys
from os.path import join, abspath, dirname


dr = abspath(dirname(abspath(__file__)))
sys.path.insert(0, join(dr, 'redditdownloader'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    exercise = PolynomialExercise()
    exercise.generate_exercise(number_of_polynomials=6, options_letters=options_letters)
