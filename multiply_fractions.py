
import math
def common_factor(a, b):
    c = math.gcd(a,b)
    if c == 1:
        print("There is no common factor between {} and {}.".format(a, b))
        return 1, a, b
    else:
        print("The greatest common factor between {} and {} is {}.".format(a, b, c))
        print("Because", c, "*", a/c, "=", a, "and", c, "*", b/c, "=", b)
        return c, a/c, b/c


def mult_f(a, b, c, d):
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
            else:
                # the 2nd fraction can be reduced. Put more work here.
    else:
        # the first is a fraction.  Put more work here.

    return 0,0,0,0,0
