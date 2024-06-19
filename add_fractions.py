def clean_two_fractions(a1, b1, c1, d1, e1, f1):


    return a1, b1, c1, d1, e1, f1


def add_two_fractions(a1, b1, c1, d1, e1, f1, kind):
    print("As a reminder if you have 5 - -2 this is the same as 5 + 2 because negative times a negative is a positive.")
    print("Similarly if you have -5 - 2, this is the same as -5 + -2, so we just add them together to get -7.")
    if kind == 1:
        if b1 == 0:
            if e1 == 0:
                print("We are adding integers, so the answer is", a1 + d1)
                return a1 + d1, 0, 1, a1 + d1, 0, 1
            else:
                print(
                    "We are adding an integer to a fraction.  So, we add the whole numbers together then put the fraction.")
                return a1 + d1, e1, f1, a1 + d1, (a1 + d1) * f1 + e1, f1
    else:
    # do something here.

    return 0, 0, 0, 0, 0


def subtract_two_fraction(a, b, c, d, e, f):
    return 0, 0, 0, 0, 0


def add_f(a, b, c, d, e, f):
    print("The first thing we need to know is if both fractions are positive or both are negative.")
    print("If not, we will turn it into a subtraction problem to make it easier.")
    if ( a > 0 or ( a == 0 and b > 0)) and ( ( d > 0) or ( d == 0 and e > 0) ):
        print("These are both positive")
    elif (a < 0 or (a == 0 and b < 0)) and ( ( d < 0) or ( d == 0 and e < 0) ):
        print("These are both negative")
    else:
        print("We will do subtraction problem.")

    return 0, 0, 0, 0, 0
