import adding_using_lcm
import clean_the_fraction
import add_two_fractions
import subtract_using_lcm

def get_rid_of_add_two_fractions(a1, b1, c1, d1, e1, f1, kind):
    print("As a reminder if you have 5 - -2 this is the same as 5 + 2 because negative times a negative is a positive.")
    print("Similarly if you have -5 - 2, this is the same as -5 + -2, so we just add them together to get -7.")
    if b1 == 0:
        if e1 == 0:
            print("We are adding integers, so the answer is", a1 + d1)
            return a1 + d1, 0, 1, a1 + d1, 0, 1
        else:
            print("We are adding an integer to a fraction.  So, we add the whole numbers together then put the fraction.")
            if kind == 1:
                return a1 + d1, e1, f1, a1 + d1, (a1 + d1) * f1 + e1, f1
            else:
                print("We have a small problem.  Here we are adding negative numbers.  Normally when we add something,",
                      "like 2 + 3 1/2 we change the 2 to 4/2 and the 3 to 6/2 then add 4/2 + 6/2 + 1/2 and get 11/2,",
                      "But, with negative numbers we have to be careful we might be tempted to do -2 - 3 1/2 as,",
                      "-4/2 - 6/2 + 1/2 - we need to make sure we keep that last fraction negative also")
                return a1 + d1, e1, f1, (a1 + d1) * f1 - e1, f1
    elif e1 == 0:
        print("We are adding a fraction to an integer.  So, we add the whole numbers together then put the fraction.")
        if a1 >= 0 and b1 >= 0:
            return a1 + d1, b1, c1, (a1 + d1) * c1 + b1, c1
        else:
            print("We have a small problem.  Here we are adding negative numbers.  Normally when we add something,",
                  "like 2 + 3 1/2 we change the 2 to 4/2 and the 3 to 6/2 then add 4/2 + 6/2 + 1/2 and get 11/2,",
                  "But, with negative numbers we have to be careful we might be tempted to do -2 - 3 1/2 as,",
                  "-4/2 - 6/2 + 1/2 - we need to make sure we keep that last fraction negative also")
            return a1 + d1, b1, c1, (a1 + d1) * c1 - b1, c1
    else:
        print("We are now adding fraction to fraction.  So, we add the whole numbers together first.")
        print("Then we add the fractions by getting common denominator.  Finally we simplify the fraction, if possible")
        print("We see the whole number is:", a1 + d1)
        a1 += d1
        whole1, num, denom = adding_using_lcm.use_least_common_denominator(a1, b1, c1, e1, f1)
        # print("Now we add the whole number we got from adding the fractions together to the original whole number", a1,
        #      "and we get", a1 + whole1)
        print("So, our answer is", whole1, str(num) + "/" + str(denom))
        if kind == 1:
            print("Our improper fraction answer is", str(whole1 * denom + num) + "/" + str(denom))
        else:
            print("Our improper fraction answer is", str(whole1 * denom - num) + "/" + str(denom))
    return whole1, num, denom, (whole1) * denom + num, denom





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
        return add_two_fractions.add_them(a, b, c, d, e, f, -1)
    elif (a > 0 or (a == 0 and b > 0)) and ((d < 0) or (d == 0 and e < 0)):
        print("The first is positive and second is negative.  Since subtracting we will do addition")
        return add_two_fractions.add_them(a, b, c, d, e, f, 1)
    else:
        print("We will do subtraction problem.")
        return subtract_using_lcm.use_least_common_denominator(a, b, c, d, e, f, "-")


