#
# eelfortune.py - Eel of Fortune
#
# Reddit: Daily Programmer - Intermediate - Challenge #223
#



# external modules

import consvowels

import itertools
import sortinsert



# main logic
#
# (function called 'problem' due to challenge format)
#

def problem(board_str, bad_str):

    # create set of letters in 'bad_str'

    bad_str_set = set(bad_str)

    # filter out all chars not from 'bad_str_set'

    board_str_chars = consvowels.explode(board_str)

    board_str_chars_final = filter(lambda x: x in bad_str_set, board_str_chars)

    # "reveal" all potentially problematic letters in 'board_str'

    board_str_compressed = consvowels.implode(board_str_chars_final)

    # check that 'bad_str' cannot be generated via 'board_str'

    return board_str_compressed == bad_str



# optional challenge #1

# retrieve the 'problem count' of
# a given 'bad word' with respect
# to a given wordfile (e.g. enable1.txt)

def problem_count(bad_str, wordfile_name):

    wordfile = open(wordfile_name)

    count = 0

    for word in wordfile:

        if problem(word, bad_str):

            count += 1

    wordfile.close()

    return count



# optional challenge #2

# helper functions for optional challenge #2

def collapse_char_tuple(char_tuple):

    res = ""

    for char in char_tuple:

        res += char

    return res


def compare_count((pc1, w1), (pc2, w2)):

    if pc1 < pc2:

        return 1

    elif pc1 == pc2:

        return 0

    else:

        return -1


# retrieve 10 5-letter strings
# with the largest 'problem counts'

def largest_10_counts(wordfile_name):

    wordfile = open(wordfile_name)

    ALPHA = "abcdefghijklmnopqrstuvxyz"

    len_5_strs = map(lambda x:collapse_char_tuple(x), list(itertools.product(ALPHA, repeat=5)))

    # initialize dictionary of problem counts

    res = {}

    for string in len_5_strs:

        res[string] = 0

    # update the dictionary per word in wordfile

    for word in wordfile:

        for string in len_5_strs:

            if problem(word, string):

                res[string] = res[string] + 1

    # retrieve strings with top 10 counts

    top_10 = sortinsert.SortList(compare_count)

    for key in res.keys():

        top_10.insert((res[key], key))

        top_10.fromList(top_10.toList()[:10])

    # return list of top 10 words

    return map(lambda (pc, word):word, top_10.toList())   

