import math
import clean_the_fraction

def use_least_common_denominator(total, num1, denom1, num2, denom2):
    # print("received total of", total)
    my_lcm = math.lcm(denom1, denom2)
    print("To get the least common denominator you need to get the LCM.  So, the LCM of", denom1, "and", denom2,
          "is equal to", my_lcm)
    print("Now what you do is take the LCM and divide it by each denominator and then multiply each numerator by that.",
          "That gives you the new numerator.  The new denominator is the LCM")
    print("In this case.  Our LCM is", my_lcm, "The first fraction was", str(num1) + "/" + str(denom1) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom1, "and we get", my_lcm/denom1, "Now multiply that by our numerator",
          num1, "and we get " + str((my_lcm * num1)//denom1) + "/" + str(my_lcm))
    print("Now we repeat the process with 2nd fraction which was " + str(num2) + "/" + str(denom2) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom2, "and we get", my_lcm // denom2,
          "Now multiply that by our second numerator",
          num2, "and we get " + str((my_lcm * num2) // denom2) + "/" + str(my_lcm))
    print("Now we have two fractions with the same denominator so now we just add the numerators.")
    print("That gives us ", total, str((my_lcm * num1)//denom1 + (my_lcm * num2)//denom2) + str("/") + str(my_lcm))
    print("Now, we could have gotten an improper fraction.  So, let's clean it up.")
    a, b, c = clean_the_fraction.clean_fraction(total, (my_lcm * num1)//denom1 + (my_lcm * num2)//denom2, my_lcm)
    return a, b, c