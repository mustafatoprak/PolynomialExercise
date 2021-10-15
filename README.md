# Polynomial Exercise Generator

This program generates a polynomial exercise including the following section:
- Consegna (the list of polynomials that are ordered in terms of exponents)
- Opzioni di risposta (the generated polynomial)
- Resoluzione guidata (the solution that list which polynomials are unordered and ordered - ascending trend and descending trend- based on the exponent values)
- Opzioni di risposto (the solution that list the correct and incorrect options besides listing the term numbers of the polynomials)


Assumptions:
- A polynomial can include minimum 2 terms and maximum 4 terms
- An exercise must include at least one polynomial with 2 terms and at least one polynomial with 4 terms
- The coefficients must be between [-12, 12] (cannot be zero)
- The exponents must be between [1, 5]
- Variable letter munst be one of [x, y, z, a, b, c]

Software requirements: Python3.6


How to run program (in the folder PolynomialExercise):
    
    python3.6 -m polynomialexercise.run_exercise

How to run tests  (in the folder PolynomialExercise):

    python3.6 -m polynomialexercise.run_tests

TODO:

The following features are not implemented since not mentioned among the requirements of the project, and may be included in the latter versions of the software.
- Property Describtor may be used to limit how to set the class variables
- Zero exponent can be added (not implemented since it was not listed as a requirement of the project)
- The software can be extended to guarantee to produce at least
- The software can be extended to guarantee to produce at least one ascending, one descending, and one unordered polynomial
- Command line argument can be included to change the polynomial generator settings
- Integration Test