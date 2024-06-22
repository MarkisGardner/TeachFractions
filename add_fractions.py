import math
import clean_the_fraction
def use_least_common_denominator(total, num1, denom1, num2, denom2):
    print("received total of", total)
    my_lcm = math.lcm(denom1, denom2)
    print("To get the least common denominator you need to get the LCM.  So, the LCM of", denom1, "and", denom2,
          "is equal to", my_lcm)
    print("Now what you do is take the LCM and divide it by each denominator and then multiply each numerator by that.",
          "That gives you the new numerator.  The new denominator is the LCM")
    print("In this case.  Our LCM is", my_lcm, "The first fraction was", str(num1) + "/" + str(denom1) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom1, "and we get", my_lcm/denom1, "Now multiply that by our numerator",
          num1, "and we get " + str(my_lcm * num1/denom1) + "/" + str(my_lcm))
    print("Now we repeat the process with 2nd fraction which was " + str(num2) + "/" + str(denom2) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom2, "and we get", my_lcm / denom2,
          "Now multiply that by our second numerator",
          num2, "and we get " + str(my_lcm * num2 / denom2) + "/" + str(my_lcm))
    print("Now we have two fractions with the same denominator so now we just add the numerators.")
    print("That gives us ", total, str(my_lcm * num1/denom1 + my_lcm * num2/denom2) + str("/") + str(my_lcm))
    print("Now, we could have gotten an improper fraction.  So, let's clean it up.")
    a, b, c = clean_the_fraction.clean_fraction(total, my_lcm * num1/denom1 + my_lcm * num2/denom2, my_lcm)


    return a, b, c



def add_two_fractions(a1, b1, c1, d1, e1, f1, kind):
    print("As a reminder if you have 5 - -2 this is the same as 5 + 2 because negative times a negative is a positive.")
    print("Similarly if you have -5 - 2, this is the same as -5 + -2, so we just add them together to get -7.")

    if b1 == 0:
        if e1 == 0:
            print("We are adding integers, so the answer is", a1 + d1)
            return a1 + d1, 0, 1, a1 + d1, 1
        else:
            print(
                "We are adding an integer to a fraction.  So, we add the whole numbers together then put the fraction.")
            if a1 >= 0 and b1 >= 0:
                return a1 + d1, e1, f1, (a1 + d1) * f1 + e1, f1
            else:
                print("We have a small problem.  Here we are adding negative numbers.  Normally when we add something,",
                    "like 2 + 3 1/2 we change the 2 to 4/2 and the 3 to 6/2 then add 4/2 + 6/2 + 1/2 and get 11/2,",
                    "But, with negative numbers we have to be careful we might be tempted to do -2 - 3 1/2 as,",
                    "-4/2 - 6/2 + 1/2 - we need to make sure we keep that last fraction negative also" )
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
        whole1, num, denom = use_least_common_denominator(a1, b1, c1, e1, f1)
        # print("Now we add the whole number we got from adding the fractions together to the original whole number", a1,
        #      "and we get", a1 + whole1)
        print("So, our answer is", whole1, str(num) + str(denom))
        print("Our improper fraction answer is", str(whole1 * denom + num) + "/" + str(denom))
    return whole1, num, denom, (whole1) * denom + num, denom


def subtract_two_fraction(a, b, c, d, e, f):
    return 0, 0, 0, 0, 0


def add_f(a, b, c, d, e, f):
    print("The first thing we need to know is if both fractions are positive or both are negative.")
    print("If not, we will turn it into a subtraction problem to make it easier.")
    if ( a > 0 or ( a == 0 and b > 0)) and ( ( d > 0) or ( d == 0 and e > 0) ):
        print("These are both positive")
        return add_two_fractions(a, b, c, d, e, f, 1)
    elif (a < 0 or (a == 0 and b < 0)) and ( ( d < 0) or ( d == 0 and e < 0) ):
        print("These are both negative")
        return add_two_fractions(a, b, c, d, e, f, -1)
    else:
        print("We will do subtraction problem.")

    return 0, 0, 0, 0, 0
