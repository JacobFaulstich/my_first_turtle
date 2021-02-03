def fac_2(user):
    are = " "
    are_not = " "
    r = user % 2
    if (r == 0):
        are = " 2 is "
    else:
        are_not = " 2 is "
    are, are_not = fac_3(user, are, are_not)
    return(are, are_not)


def fac_3(user, are, are_not):
    r = user % 3
    if (r == 0):
        are = are + " 3 is a "
    else:
        are_not = are_not + " 3 is "
    are, are_not = fac_5(user, are, are_not)
    return(are, are_not)


def fac_5(user, are, are_not):
    r = user % 5
    if (r == 0):
        are = are + " 5 is "
    else:
        are_not = are_not + " 5 is "
    return(are, are_not)


user = input(" Give me an integer: ")
user = int(user)
are, are_not = fac_2(user)
message = are + "a factor of " + str(user) + ": " + are_not + " not a factor of " + str(user)
print(message)