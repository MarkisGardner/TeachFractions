import math
import clean_the_fraction

def check_which_is_bigger(whole1, num1, denom1, whole2, num2, denom2):
    if abs(whole1) > abs(whole2):
        return 1
    elif abs(whole1) < abs(whole2):
        return -1
    elif abs(num1) > abs(num2):
        return 1
    elif abs(num1) == abs(num2):
        return 0
    else:
        return -1


def subtract_them(whole1, num1, denom1, whole2, num2, denom2, sign, SIGNTYPE):
    print(whole1, num1, denom1, whole2, num2, denom2, sign, SIGNTYPE)
    if num1 < num2:
        if whole1 > 0:
            num1 = num1 + denom1
            whole1 = whole1 - 1
        else:
            num1 = num1 + denom1
            whole1 = whole1 + 1
    if sign == 1:
        print("here2", whole1, num1, denom1, whole2, num2, denom2, sign, SIGNTYPE)
        if SIGNTYPE == "-":
            return whole1 - whole2, num1 - num2, denom1
        else:
            if whole1 != whole2:
                return whole1 + whole2, num1 - num2, denom1
            else:
                return 0, num1 + num2, denom1
    elif whole1 - whole2 == 0:
        return whole1 - whole2, num1 - num2, denom1
    else:
        if whole1 < 0:
            if SIGNTYPE == "+":
                return whole1 - whole2, num1 - num2, denom1
            else:
                return whole1 + whole2, num1 - num2, denom1
        else:
            if SIGNTYPE == "-":
                return -1 * whole1 + whole2, num1 - num2, denom1
            else:
                return whole1 + whole2, num1 - num2, denom1

def use_least_common_denominator(whole1, num1, denom1, whole2, num2, denom2, SIGNTYPE):
    print("The first thing we want to do is check to see if we have a problem like -1 - -2")
    print("If we do then we want to change that to -1 + 2")
    if SIGNTYPE == "-":
        if whole2 < 0:
            SIGNTYPE = "+"
            whole2 = whole2 * -1
        elif num2 < 0:
            num2 = num2 * -1
            SIGNTYPE = "+"
    print("The first thing we need to do is get the common denominator.  This will help know which fraction is larger.")
    my_lcm = math.lcm(denom1, denom2)
    print("To get the least common denominator you need to get the LCM.  So, the LCM of", denom1, "and", denom2,
          "is equal to", my_lcm)
    print("Now what you do is take the LCM and divide it by each denominator and then multiply each numerator by that.",
          "That gives you the new numerator.  The new denominator is the LCM")
    print("In this case.  Our LCM is", my_lcm, "The first fraction was", str(num1) + "/" + str(denom1) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom1, "and we get", my_lcm//denom1, "Now multiply that by our numerator",
          num1, "and we get " + str((my_lcm * num1)//denom1) + "/" + str(my_lcm))
    print("Now we repeat the process with 2nd fraction which was " + str(num2) + "/" + str(denom2) + ".")
    print("Now we divide our LCM", my_lcm, "by", denom2, "and we get", my_lcm // denom2,
          "Now multiply that by our second numerator",
          num2, "and we get " + str((my_lcm * num2) // denom2) + "/" + str(my_lcm))
    num1 = (my_lcm * num1)//denom1
    denom1 = my_lcm
    num2 = (my_lcm * num2)//denom2
    denom2 = my_lcm
    print("Now we have two fractions with the same denominator so now we just subtract the numerators.")
    # print("At this point - we have")
    # print(whole1, num1, denom1, whole2, num2, denom2)
    print("We have to decide which fraction is larger because it is much easier to subtract the two like integers.")
    print("Example:  When you have 2 - 5, it is better to do 5 - 2 and use the sign of the larger, since 5 is larger")
    print("We use the sign of 5 which is negative.  So, 5 - 2 = 3 but the sign is negative so make it -3.")
    print("We will do the same with fractions.")
    larger = check_which_is_bigger(whole1, num1, denom1, whole2, num2, denom2)
    if larger > 0:
        print("We see that fraction 1:",whole1, str(num1) + "/" + str(denom1), "is larger than", whole2, str(num2) + "/" + str(denom2))
        a, b, c = subtract_them(whole1, num1, denom1, whole2, num2, denom2, larger, SIGNTYPE)
    elif larger == 0:
        print("we see the two fractions are equal so the answer is 0.")
        return 0, 0, 1, 0, 1
    else:
        print("We see that fraction 1:", whole1, str(num1) + "/" + str(denom1), "is smaller than", whole2,
              str(num2) + "/" + str(denom2))
        whole1, whole2 = whole2, whole1
        num1, num2 = num2, num1
        print("So, let's flip them and now we have the following:")
        print("Now we have", whole1, str(num1) + "/" + str(denom1), SIGNTYPE, (whole2), str(num2) + "/" + str(denom2))
        #print("We see that fraction 1:", whole1, str(num1) + "/" + str(denom1), "is larger than", whole2,
        #     str(num2) + "/" + str(denom2), "as long as you ignore the sign")
        a, b, c = subtract_them(whole1, num1, denom1, whole2, num2, denom2, larger, SIGNTYPE)

        # print("here we have the answer:", a, str(b) + "/" + str(c))
    #print("That gives us ", total, str((my_lcm * num1)//denom1 + (my_lcm * num2)//denom2) + str("/") + str(my_lcm))
    # print("Now, we could have gotten an improper fraction.  So, let's clean it up.")
    #a, b, c = clean_the_fraction.clean_fraction(total, (my_lcm * num1)//denom1 + (my_lcm * num2)//denom2, my_lcm)
    if a < 0:
        return a, b, c, a * c - b, c
    else:
        return a, b, c, a * c + b, c