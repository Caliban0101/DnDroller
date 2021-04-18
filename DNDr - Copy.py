from random import randint
from re import findall

#dice rolling program
#asking for input
str = input("""
Welcome to DnD dice roller! 
type 'quit' to close.
What would you like to roll?

""")

running = True
while running == True:
#if quit is found in the input the program ends
    if str.find('quit') != -1:
        running = False
        break
#otherwise, numbers is a list of numbers in the string
#lsint is that list converted to integers
    numbers = findall(r'\d+', str)
    lsint = [int(i) for i in numbers]
#if there are no numbers if the string
    if len(lsint) == 0:

        b = """sorry, I require numerical digits to funtion.
Or type quit."""

        b = 'you must choose dice to roll, or type quit'
#if the input is something like 'a d6'

    elif len(lsint) == 1:
        b = randint(1,lsint[0])
#normal case 6d6 etc.
    elif len(lsint) > 1:
        a = lsint[0]
        b = randint(1,lsint[1])
        while a > 1:
            b = b + randint(1,lsint[1])
            a = a - 1
    print(b)
    str = input("""What dice would you like to roll?
type quit to close
""")
print('Bye!')

