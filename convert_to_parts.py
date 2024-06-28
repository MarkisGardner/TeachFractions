def first_part(text, t_type):
    # print(text)
    first = len(text)-len(text.lstrip())
    # Now we know the first position of the first number
    last = text.find(t_type)
    # Now we know the position of the last character of first part
    fp_str = text[first:last]
    fp_str = fp_str.strip()
    # print("fp_str is {}".format(fp_str))
    pos_of_space = fp_str.find(' ')
    if (pos_of_space == -1) and (fp_str.find('/') != -1):
        # Only a fraction - no whole number
        a = 0
    elif pos_of_space == -1:
        # Only an integer - no fraction
        a = fp_str
    else:
        a = int(fp_str[0:pos_of_space])
    # print("A is {}".format(a))

    pos_of_slash = fp_str.find('/')
    # print("pos_of_slash is {}".format(pos_of_slash))
    if pos_of_slash == -1:
        b = 0
        c = 1
    else:
        if a != 0:
            b = int(fp_str[pos_of_space:pos_of_slash])
        else:
            b = int(fp_str[0:pos_of_slash])
        c = int(fp_str[pos_of_slash+1:])
    a = int(a)
    b = int(b)
    c = int(c)
    return a, b, c

def second_part(text, t_type):
    # print(text)
    first = text.find(t_type) + 2
    # Now we know the position of the first character of the second part
    last = len(text)
    # Now we know the position of the last character of the second part
    sp_str = text[first:last]
    # print("sp_str is {}".format(sp_str))
    sp_str = sp_str.lstrip()
    pos_of_space = sp_str.find(' ')
    if (pos_of_space == -1) and (sp_str.find('/') != -1):
        # there is no whole number and there is a fraction
        d = 0
    elif (pos_of_space == -1):
        # there is no fraction part so it is an integer.
        d=sp_str
    else:
        d = int(sp_str[0:pos_of_space])
    # print("D is {}".format(d))
    pos_of_slash = sp_str.find('/')
    if pos_of_slash == -1:
        e = 0
        f = 1
    else:
        if pos_of_space != 0:
            e = int(sp_str[pos_of_space+1:pos_of_slash])
        else:
            e = int(sp_str[0:pos_of_slash])
        f = int(sp_str[pos_of_slash+1:])
    d = int(d)
    e = int(e)
    f = int(f)
    return d, e, f

def ctp(text, t_type):
    # print("I received",text, t_type)
    a, b, c = first_part(text, t_type)
    d, e, f = second_part(text, t_type)
    # print("a is {}".format(a), "b is {}".format(b), "c is {}".format(c))
    # print("d is {}".format(d), "e is {}".format(e), "f is {}".format(f))
    # test
    return a, b, c, d, e, f
