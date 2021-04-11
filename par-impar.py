#oddoreven
print ("What number are you thinking")

answer = 'y'

while answer != 'n':

    number = int(input())

    if (number % 2) == 0:
        print ("That's an even number! Have another?")
    else:
        print ("That's an odd number! Have another?")

    answer = input()