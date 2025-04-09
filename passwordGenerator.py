from tkinter import *
import random

def generatePassword(name, secondName, birthDate):
    amount_of_special = random.randint(2,2)
    password = ""
    password += name[0].upper()
    random_indent = random.randint(0 ,len(secondName) - 1)
    password += secondName[:random_indent]
    i = 0
    for letter in secondName.title():
        if i == random_indent:
            special_symbol = random.randint(33, 41)
            print(special_symbol)
            password += chr(special_symbol)
            i+=1
        else:
            i += 1

    password += secondName[random_indent:]

    password += birthDate

    if amount_of_special > 1:
        special_symbol = random.randint(33, 41)
        password += chr(special_symbol)

    print(password)

    return password

if __name__ == "__main__":
    generatePassword("Will", "Jones", "2008")