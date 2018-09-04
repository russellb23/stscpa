""" Rock, Paper & Sciccors game in python """
import random
from collections import Counter

urname = input("Please enter your name: ")

result = list()

m = 1
while m == 1:

    print("Game states are any of the following: \n 1) Rock \n 2) Sciccors \n 3) Paper")
    comp_choice = random.randint(1,3)
    human_cjoice = int(input(("What's your daemon!?")))
    print("Your state: {} \nComputer state: {}".format(human_cjoice, \
            comp_choice).rjust(18))
    if comp_choice == human_cjoice:
        result.append('Tie')
        print("It's a tie")
    
    elif comp_choice > human_cjoice:
        if comp_choice == 3 and human_cjoice == 1:
            result.append('Computer')
            print("Computer won!")
        elif comp_choice == 3 and human_cjoice == 2:
            result.append(urname)
            print("{} won!".format(urname))
        elif comp_choice == 2 and human_cjoice == 1:
            result.append(urname)
            print("{} won!".format(urname))
    
    elif comp_choice < human_cjoice:
        if comp_choice == 2 and human_cjoice == 3:
            result.append('Computer')
            print("Computer won!")
        elif comp_choice == 1 and human_cjoice == 2:
            result.append('Computer')
            print("Computer won!")
        elif comp_choice == 1 and human_cjoice == 3:
            result.append(urname)
            print("{} won!".format(urname))

    c = input("Type[Enter/N]: ")
    if c.lower() == 'y':
        m = 1
    elif c.lower() == 'n':
        result_ = Counter(result)
        print("=="*5, "Results", "=="*5)
        for k, v in result_.items():
            print("{}: {}".format(k,v).rjust(18))
        print("=="*7, "=="*7)
        m = 0
