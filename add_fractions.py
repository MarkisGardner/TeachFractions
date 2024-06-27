import math
import clean_the_fraction
import adding_using_lcm
import add_two_fractions
import subtract_using_lcm



def subtract_two_fractions(a, b, c, d, e, f):
    return 0, 0, 0, 0, 0


def add_f(a, b, c, d, e, f):
    print("The first thing we need to know is if both fractions are positive or both are negative.")
    print("If not, we will turn it into a subtraction problem to make it easier.")
    if ( a > 0 or ( a == 0 and b > 0)) and ( ( d > 0) or ( d == 0 and e > 0) ):
        print("These are both positive")
        return add_two_fractions.add_them(a, b, c, d, e, f, 1)
    elif (a < 0 or (a == 0 and b < 0)) and ( ( d < 0) or ( d == 0 and e < 0) ):
        print("These are both negative")
        return add_two_fractions.add_them(a, b, c, d, e, f, -1)
    else:
        print("We will do subtraction problem.")
        return subtract_using_lcm.use_least_common_denominator(a, b, c, d, e, f)
    # return 0, 0, 0, 0, 0
