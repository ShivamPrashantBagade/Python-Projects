from random import *

n = int(input("Enter number of tosses:"))


def toss():
    outputList = []

    for i in range(1, n+1):
        a = randint(0, 1)
        outputList.append(a)

    finalOutput = []
    for i in outputList:
        if i == 1:
            finalOutput.append('Head')
        else:
            finalOutput.append("Tale")
    print(finalOutput)

    head_count = 0
    tale_count = 0

    for i in finalOutput:
        if i == 'Head':
            head_count = head_count + 1
        else:
            tale_count = tale_count + 1

    print(" ")
    print(f"Number of heads is {head_count} and tail is {tale_count}")
    print(" ")

    print(f"Probability of head is {head_count/n}")
    print(f"Probability of tail is {tale_count/n}")


toss()
