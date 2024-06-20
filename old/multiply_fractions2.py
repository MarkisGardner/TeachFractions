
import math
def common_factor(a, b):
    c = 1
    b=int(b)
    print(type(a), type(b), type(c))
    c = math.gcd(a,b)
    if c == 1:
        print("There is no common factor between {} and {}.".format(a, b))
        return 1, a, b
    else:
        print("The greatest common factor between {} and {} is {}.".format(a, b, c))
        print("Because", c, "*", a/c, "=", a, "and", c, "*", b/c, "=", b)
        return c, a/c, b/c


def process_for_multiplying_numerator_by_2nd_fraction(a, b, c, d):
    print("This is better than multiplying first because it makes the numbers smaller.")
    e, f, g = common_factor(a, d)
    if e == 1:
        print("We see that it does not reduce, so now we multiply the constant", a,
              "buy the numerator of the second fraction", c)
        print("So", a, "*", c, "/", d, "is", str(a*c) + "/" + str(d))
        print("Now, that is the improper fraction answer")
        if a * c < d:
            print("Because the numerator is less than the denominator it is also the regular fraction answer.")
            return 0, a*c, d, a*c, d
        else:
            print("As you can see the numerator is bigger than the denominator, many teachers do not like that.")
            print("So, it is important for you to know how to convert that to a proper fraction.")
            print("There are two steps.  1.  Divide the numerator by the denominator.")
            print("Keep the number of times it divides and the remainder.")
            print("As we can see" + str(a*c) + "divided by", str(d), "can be done" + str((a*c)//d), "times.")
            print("The remainder is", (a*c)%d)
            return (a*c)//d, (a*c)%d, d, a*c, d
    else:
        print(e,"is the largest common factor for both", a, "and", d, "so we need to divide both by", e)
        # put more work here.
        print("Since" + str(a) + "divided by" + str(e) + "is" + str(a / e) +
              "and " + str(d) + "divided by " + str(e) + "is" + str(d/e))
        a = a / e
        d = d / e
        print("So, now we have ",a, "*" + str(c) + "/" + str(d))
        print(a,"*", c, "is", a*c)
        print("So, the improper fraction answer is", str(a*c) +"/" + str(d))
        if (a*c) < d:
            print("Since", a*c, "is smaller than", d, "the standard fraction is the same answer also.")
            return 0, a*c, d, a*c, d
        elif (a*c) == d:
            print("Since the numerator and the denominator is the same - we get 1.")
            return 1, 0, 1, 1, 1
        else:
            print("Since", a*c, "is bigger than", d, "we need to find out how many times", d,
                  "will go into", a*c, "and find the remainder.")
            print("It goes", (a * c)//d, "times and the remainder is", (a * c)%d)
            return (a * c)//d, (a * c)%d, d, a*c, d


def mult_f(a, b, c, d):
    print(type(a))
    if b == 1:
        if d == 1:
            print("Neither have a denominator so we just multiply the two numbers", a, c)
            print("we get", a * c)
            return a * c, 0, 1, a * c, 1
        else:
            print("The first number is not a fraction so we need to just multiply by the second fraction")
            print("Before we multiply we first want to see if we can reduce the second fraction.")
            e, f, g = common_factor(c, d)
            if e == 1:
                print("We see that the 2nd fraction cannot be reduced.  So, now we see if the constant", a,
                      "can reduce with the denominator with the second fraction", d)
                print("This is better than multiplying first because it makes the numbers smaller.")
                e, f, g = common_factor(a, d)
                if e == 1:
                    print("We see that it does not reduce, so now we multiply the constant", a,
                          "buy the numerator of the second fraction", c)
                    print("So", a, "*", c, "/", d, "is", str(a*c) + "/" + str(d))
                    print("Now, that is the improper fraction answer")
                    if a * c < d:
                        print("Because the numerator is less than the denominator it is also the regular fraction answer.")
                        return 0, a*c, d, a*c, d
                    else:
                        print("As you can see the numerator is bigger than the denominator, many teachers do not like that.")
                        print("So, it is important for you to know how to convert that to a proper fraction.")
                        print("There are two steps.  1.  Divide the numerator by the denominator.")
                        print("Keep the number of times it divides and the remainder.")
                        print("As we can see" + str(a*c) + "divided by", str(d), "can be done" + str((a*c)//d), "times.")
                        print("The remainder is", (a*c)%d)
                        return (a*c)//d, (a*c)%d, d, a*c, d
                else:
                    print(e,"is the largest common factor for both", a, "and", d, "so we need to divide both by", e)
                    # put more work here.
                    print("Since" + str(a) + "divided by" + str(e) + "is" + str(a / e) +
                          "and " + str(d) + "divided by " + str(e) + "is" + str(d/e))
                    a = a / e
                    d = d / e
                    print("So, now we have ",a, "*" + str(c) + "/" + str(d))
                    print(a,"*", c, "is", a*c)
                    print("So, the improper fraction answer is", str(a*c) +"/" + str(d))
                    if (a*c) < d:
                        print("Since", a*c, "is smaller than", d, "the standard fraction is the same answer also.")
                        return 0, a*c, d, a*c, d
                    elif (a*c) == d:
                        print("Since the numerator and the denominator is the same - we get 1.")
                        return 1, 0, 1, 1, 1
                    else:
                        print("Since", a*c, "is bigger than", d, "we need to find out how many times", d,
                              "will go into", a*c, "and find the remainder.")
                        print("It goes", (a * c)//d, "times and the remainder is", (a * c)%d)
                        return (a * c)//d, (a * c)%d, d, a*c, d

            else:
                # the 2nd fraction can be reduced. Put more work here.
                print("Now, in this case, the 2nd fraction can be reduced.  We can see that", e,
                      "divides both", c,"and", d)
                c = c / e
                d = d / e
                print("So, let's reduce that.  We will divide top and bottom by", e, "to get us " + str(c) +
                      "/" + str(d))
                # Check the paste here
                print("So, now we see if the constant", a,
                      "can reduce with the denominator with the second fraction", d)
                print("This is better than multiplying first because it makes the numbers smaller.")
                e, f, g = common_factor(a, d)
                if e == 1:
                    print("We see that it does not reduce, so now we multiply the constant", a,
                          "buy the numerator of the second fraction", c)
                    print("So", a, "*", c, "/", d, "is", str(a * c) + "/" + str(d))
                    print("Now, that is the improper fraction answer")
                    if a * c < d:
                        print(
                            "Because the numerator is less than the denominator it is also the regular fraction answer.")
                        return 0, a * c, d, a * c, d
                    else:
                        print(
                            "As you can see the numerator is bigger than the denominator, many teachers do not like that.")
                        print("So, it is important for you to know how to convert that to a proper fraction.")
                        print("There are two steps.  1.  Divide the numerator by the denominator.")
                        print("Keep the number of times it divides and the remainder.")
                        print("As we can see" + str(a * c) + "divided by", str(d), "can be done" + str((a * c) // d),
                              "times.")
                        print("The remainder is", (a * c) % d)
                        return (a * c) // d, (a * c) % d, d, a * c, d
                else:
                    print(e, "is the largest common factor for both", a, "and", d, "so we need to divide both by", e)
                    # put more work here.
                    print("Since" + str(a) + "divided by" + str(e) + "is" + str(a / e) +
                          "and " + str(d) + "divided by " + str(e) + "is" + str(d / e))
                    a = a / e
                    d = d / e
                    print("So, now we have ", a, "*" + str(c) + "/" + str(d))
                    print(a, "*", c, "is", a * c)
                    print("So, the improper fraction answer is", str(a * c) + "/" + str(d))
                    if (a * c) < d:
                        print("Since", a * c, "is smaller than", d, "the standard fraction is the same answer also.")
                        return 0, a * c, d, a * c, d
                    elif (a * c) == d:
                        print("Since the numerator and the denominator is the same - we get 1.")
                        return 1, 0, 1, 1, 1
                    else:
                        print("Since", a * c, "is bigger than", d, "we need to find out how many times", d,
                              "will go into", a * c, "and find the remainder.")
                        print("It goes", (a * c) // d, "times and the remainder is", (a * c) % d)
                        return (a * c) // d, (a * c) % d, d, a * c, d


                # return 0,0,0,0,0
    else:
        # the first is a fraction.  Put more work here.
        print("Working on this later")
        return 0,0,0,0,0
