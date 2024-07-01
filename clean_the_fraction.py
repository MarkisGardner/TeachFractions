def clean_fraction(a1, b1, c1):
    # this will allow improper fractions but will not allow mixed fractions that are also improper fractions.
    # example:  it will change 1 3/2 to 2 1/2 but will keep 7/2 the same.
    if a1 == 0:
        if abs(b1) >= c1:
            print(str(b1) + "/" + str(c1), "is a valid improper fraction.")
        else:
            print(str(b1) + "/" + str(c1), "is a valid proper fraction.")
    else:
        if b1 >= c1:
            print(a1, str(b1) + "/" + str(c1), "is not a valid improper fraction.")
            if a1 < 0:
                print("So we will change it to: ", a1 - b1 // c1, str(b1 % c1) + "/" + str(c1))
                print("We do that by taking", b1,"and dividing it by", c1, "taking only the integer portion and subtracting it from", a1)
                print("then the remainder is the new numerator.  In this case", str(b1) + "/" + str(c1), "gives us", b1 // c1,
                      "with remainder", b1 % c1)
                print("So, subtract", b1 // c1, "from", a1, "and take the remainder as the new numerator.")
                a1 -= b1 // c1
                b1 = b1 % c1
            else:
                print("So we will change it to: ", a1 + b1 // c1, str(b1 % c1) + "/" + str(c1))
                print("We do that by taking", b1, "and dividing it by", c1,
                      "taking only the integer portion and adding it to", a1)
                print("then the remainder is the new numerator.  In this case", str(b1) + "/" + str(c1), "gives us",
                      b1 // c1,
                      "with remainder", b1 % c1)
                print("So, add", b1 // c1, "to", a1, "and take the remainder as the new numerator.")
                a1 += b1 // c1
                b1 = b1 % c1
        else:
            print(a1, str(b1) + "/" + str(c1), "is a valid proper fraction.")

    return a1, b1, c1