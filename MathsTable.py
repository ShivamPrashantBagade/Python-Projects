def MathsTable():

    user_input1 = int(input("Table of :"))
    user_input2 = int(input("Till number :"))

    for n in range(1, user_input2+1):

        print(f"{user_input1} x {n} = {n*user_input1}")


MathsTable()
