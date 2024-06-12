# This is a sample Python script.
# import os
import sys
import convert_to_parts
import add_fractions
import subtract_fractions
import multiply_fractions
import divide_fractions

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def instructions():
    # This will give the instructions if there is an error or if called.
    print("This script will teach you how to add, subtract, multiply or divide fractions.")
    print("This script can accept two fractions in the form a b/c or b/c or a")
    print("Please enter two fractions and an operator between them.  The operator must have spaces around it")
    print("Example:  2 3/5 + 3/7")
    print("You can even put negative signs like: -3 4/5 + -3/4")
    print("The acceptable operators are +,-,* and /")


def is_valid(t_problem):
    # this function makes sure there are no other characters in the problem.
    allowed_set = " 0123456789+-*/"
    for char in t_problem:
        if char not in allowed_set:
            return False
    return True


def check_type(t_problem):
    # this function makes sure there is only one +, -, * or / in the problem.
    # also because subtraction and negative are two different items I had to check that
    # also because / could be part of a fraction I had to check that.
    # it will also check to see if it is a valid fraction problem
    print("I received:", t_problem)
    ct_plus = t_problem.count("+")
    ct_minus = t_problem.count(" - ")
    ct_multiply = t_problem.count("*")
    ct_divide = t_problem.count(" / ")
    if (ct_multiply + ct_minus + ct_divide + ct_plus) == 1:
        t_valid = is_valid(t_problem)
        if not t_valid:
            return "ERROR"
        elif ct_plus == 1:
            return "+"
        elif ct_minus == 1:
            return " - "
        elif ct_divide == 1:
            return " / "
        else:
            return "*"
    else:
        return "ERROR"


def print_the_solution(coeff, numer, denom, imp_num, imp_den):
    if coeff == 0:
        print("The answer is:", str(numer)+"/"+str(denom))
        print("since there is no whole number part there is no improper fraction solution.")
    else:
        print("The answer is:", coeff, str(numer)+"/"+str(denom))
        print("The improper fraction solution is", str(imp_num)+"/"+str(imp_den))


problem = 0
while problem != "QUIT":
    problem = input(
        "Please enter an addition/subtraction/multiplication/division problem using fractions or hit enter for "
        "instructions: ")
    f_type = check_type(problem)
    print("it is type", f_type)
    if f_type == "ERROR":
        instructions()
        print("Program terminated")
        sys.exit(0)
    a, b, c, d, e, f = convert_to_parts.ctp(problem, f_type)
    if f_type == "+":
        g, h, i, j, k = add_fractions.add_f(a, b, c, d, e, f)
    elif f_type == "-":
        g, h, i, j, k = subtract_fractions.sub_f(a, b, c, d, e, f)
    elif f_type == "*":
        g, h, i, j, k = multiply_fractions.mult_f(a, b, c, d, e, f)
    else:
        g, h, i, j, k = divide_fractions.div_f(a, b, c, d, e, f)

    print_the_solution(g, h, i, j, k)