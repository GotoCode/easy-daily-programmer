#
# eelfortune.py - Eel of Fortune
#
# Reddit: Daily Programmer - Intermediate - Challenge #223
#



# helper functions


def LCS(str_1, str_2, i, j, memo):

    # simple bounds-check

    if (i < 0) or (j < 0) or (i >= len(str_1)) or (j >= len(str_2)):

        return 0

    # check if solution already found before...

    if memo[i][j] != None:
        
        return memo[i][j]

    # else, solve for value of memo[i][j]

    if str_1[i] == str_2[j]:

        memo[i][j] = 1 + LCS(str_1, str_2, i+1, j+1, memo)

        return memo[i][j]

    else:

        memo[i][j] = max(LCS(str_1, str_2, i+1, j, memo), LCS(str_1, str_2, i, j+1, memo))

        return memo[i][j]



def overlap_edges(str_1, str_2):

    candidate_chars = str_2

    for char in str_1:

        if char in str_2:

            if candidate_chars == "" or char != candidate_chars[0]:

                return True
            
            else:

                candidate_chars = candidate_chars[1:]

    return False



# main logic
#
# (function called 'problem' due to challenge format)
#

def problem(board_str, bad_str):

    # initialize 'memo table'

    memo = []

    for i in range(len(board_str)):

        memo.append([None] * len(bad_str))

    # compute length of 'longest common subsequence' (LCS)

    len_lcs = LCS(board_str, bad_str, 0, 0, memo)

    # check that 'no edges of matching cross'

    if not overlap_edges(board_str, bad_str):

        return len_lcs == len(bad_str)

    else:

        return False



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

    return count
