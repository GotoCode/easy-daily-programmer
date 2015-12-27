#
# brokenkeyboard.py - Solver for the "broken keyboard" problem
#
# Reddit: Daily Programmer - Easy - Challenge #237
#
# ABANDONED... - Ballooning complexity, poorly-thought-out design, not well understood problem...
#

# external modules

import consvowels



# sample input

# 3
# abcd
# qwer
# hjklo



# sample output

# abcd  = bacaba
# qwer  = ewerer
# hjklo = kolokolo



# helper functions

def load_dict(filename):   # very, very slow function - (O(n*log(n))) complexity

    # create a (char, set of words) store,
    # such that <set of words> contains
    # all words which contain <char> in them

    res = {}

    data_file = open(filename)

    for word in data_file:

        for char in word.strip():

            res[char] = res.get(char, set()).union(set([word.strip(), None]))

    return res


def load_words(filename):   # O(n) complexity

    # create a list of all valid words

    res = []

    data_file = open(filename)

    for word in data_file:

        res.append(word.strip())

    return res


def get_charlist(chars, wordlist):

    res = []

    max_len = 0

    chars_list = consvowels.explode(chars)

    for word in wordlist:

        member_chars = None

        print word
        max_len = len(word)

    return res


def typeable_word(word, char_string):

    char_list = consvowels.explode(char_string)

    word_char_list = consvowels.explode(word)

    for char in char_list:

        word_char_list = filter(lambda c:not (c in char_list), word_char_list)

    if word_char_list == []:
        
        return True
    
    else:
        
        return False



# can the chars in <letters> generate <word>?

def can_generate(letters, word):

    available_chars = set(letters)
    word_chars      = set(word)

    diff = word_chars.difference(available_chars)

    if (len(list(diff)) == 0):

        return True

    else:

        return False



def compare_pair((w1, l1), (w2, l2)):

    if l1 > l2:
        return (w1, l1)
    else:
        return (w2, l2)



# main logic

def main():

    char_set_map = load_words("/usr/share/dict/words")

    num_lines = int(raw_input("How many input lines? "))

    for i in range(0, num_lines):

        letters = raw_input("Enter available letters: ")

        letters_list = consvowels.explode(letters)

        final_set_map = char_set_map

        final_set_map = filter(lambda w:can_generate(letters, w), final_set_map)

        final_set_map_pairs = map(lambda w:(w, len(w)), final_set_map)

        longest_word, len_longest = reduce(compare_pair, final_set_map_pairs)

        print longest_word
        
    
