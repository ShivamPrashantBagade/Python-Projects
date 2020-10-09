import random


def strong_password_generator():

    user_input = int(input("Enter length of password:"))

    collection = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '%', '^', '&', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    password_list = []
    password = ""

    for i in range(user_input):

        a = random.choice(collection)
        password_list.append(a)

    password = password.join(password_list)

    print(password)


strong_password_generator()
