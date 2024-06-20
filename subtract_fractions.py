def add_two_fractions(a1, b1, c1, d1, e1, f1, kind):
    print("As a reminder if you have 5 - -2 this is the same as 5 + 2 because negative times a negative is a positive.")
    print("Similarly if you have -5 - 2, this is the same as -5 + -2, so we just add them together to get -7.")
    if kind == 1:
        if b1 == 0:
            if e1 == 0:
                print("We are adding integers, so the answer is", a1 + d1)
                return a1 + d1, 0, 1, a1 + d1, 0, 1
            else:
                print("We are adding an integer to a fraction.  So, we add the whole numbers together then put the fraction.")
                return a1 + d1, e1, f1, a1 + d1, (a1 + d1) * f1 + e1, f1
    else:
        print()
        # do something here.

    return 0, 0, 0, 0, 0


def subtract_two_fraction(a, b, c, d, e, f):


    return 0, 0, 0, 0, 0

def sub_f(a, b, c, d, e, f):
    print("The first thing we need to know is if both fractions are positive or both are negative.")
    print("If not, we will turn it into a addition problem to make it easier.")
    if (a < 0 or (a == 0 and b < 0)) and ((d > 0) or (d == 0 and e > 0)):
        print("First is negative and second is positive.  Since subtracting we will do addition")
        if d > 0:
            print("We will treat", d, "as", -1 * d, "and just add the two fractions.")
            d = d * (-1)
        else:
            print(" So, we will treat", e, "as", -1 * e, "and just add the two fractions.")
            e = e * (-1)
        add_two_fractions(a, b, c, d, e, f, -1)
    elif (a > 0 or (a == 0 and b > 0)) and ((d < 0) or (d == 0 and e < 0)):
        print("The first is positive and second is negative.  Since subtracting we will do addition")
        add_two_fractions(a, b, c, d, e, f, 1)
    else:
        print("We will do subtraction problem.")
        subtract_two_fraction(a, b, c, d, e, f)
    return 0, 0, 0, 0, 0

