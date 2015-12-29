#
# consvowels.py - Consonants & Vowels
#
# Reddit: Daily Programmer
#
# Easy - Challenge #238
#

# Example Input:  cvcvccv
# Example Output: telamno


# imported modules

import random


# constants

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


# helper functions

def explode(string):

    res = []

    for char in string:

        res += char

    return res


def implode(char_list):

    return "".join(char_list)


VOWELS_LIST = explode(VOWELS)
CONSONANTS_LIST = explode(CONSONANTS)


def replaceCV(cv_char):

    if cv_char == " ":
        return " "

    res = cv_char

    if cv_char in "Cc":
        
        res = random.sample(CONSONANTS_LIST, 1)[0]
    
    else:
        
        res = random.sample(VOWELS_LIST, 1)[0]

    if cv_char in "CV":

        res = res.capitalize()

    return res


# *extra* helper functions

CAP_VOWELS_LIST = map(lambda s:s.capitalize(), VOWELS_LIST)
CAP_CONSONANTS_LIST = map(lambda s:s.capitalize(), CONSONANTS_LIST)


def convertName(name):

    cv_final = ""
    
    for char in name:

        if char in CAP_VOWELS_LIST:

            cv_final += "V"

        elif char in CAP_CONSONANTS_LIST:

            cv_final += "C"

        elif char in VOWELS:

            cv_final += "v"

        elif char in CONSONANTS:

            cv_final += "c"

        else:

            cv_final += char

    return cv_final
            



# main logic

def main():

    query = ""

    query = raw_input("Enter 'c-v' pattern: ")

    print

    while query != "quit":

        cvc_list = explode(query)

        cvc_count = sum(map(lambda x:1, filter(lambda x:x in "CcVv", cvc_list)))

        if (cvc_count != len(cvc_list)):

            raise RuntimeError, "Error: Improperly formatted input string..."

        res_list = map(replaceCV, cvc_list)

        final = implode(res_list)

        print final, "\n"

        query = raw_input("Enter 'c-v' pattern: ")

        print



# alternate main logic (name conversion)

def main2():

    query = ""

    query = raw_input("Enter name: ")

    print

    while query != "quit":

        cvc_list = explode(convertName(query))

        res_list = map(replaceCV, cvc_list)

        final = implode(res_list)

        print final, "\n"

        query = raw_input("Enter name: ")

        print
