def CheckPlaindrome():

    user_input = input("Enter a word:")

    a = user_input
    b = a.lower()

    if b == b[::-1]:
        print("It is a Plaindrome")
    else:
        print("Not a Plaindrome")


CheckPlaindrome()
