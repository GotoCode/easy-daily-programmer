#
# vhsrecord.py - Implementation of VHS Recording Problem
#
# Reddit: Daily Programmer - Intermediate - Challenge #242
#


# external modules

import copy


# helper functions

def before(x, y):

    str_x = str(x)
    str_y = str(y)

    num_digits_x = len(str_x)
    num_digits_y = len(str_y)

    if num_digits_x == num_digits_y:

        return x < y

    elif num_digits_x > num_digits_y:

        if   num_digits_x == 4: return True
        elif num_digits_x == 3: return False
        elif num_digits_x == 2: return False
        elif num_digits_x == 1: return False

    else:

        if   num_digits_x == 3: return True
        elif num_digits_x == 2: return True
        elif num_digits_x == 1: return True
        elif num_digits_x == 0: return True


def after(x, y):

    return before(y, x)


def between(x, y, z):

    return after(x, y) and before(x, z)


def collide((start_1, stop_1), (start_2, stop_2)):

    btwn_1 = between(start_2, start_1, stop_1)
    btwn_2 = between(stop_2, start_1, stop_1)
    btwn_3 = between(start_1, start_2, stop_2)
    btwn_4 = between(stop_1, start_2, stop_2)

    return btwn_1 or btwn_2 or btwn_3 or btwn_4


def check_collision(interval, interval_list):

    for other_interval in interval_list:

        if collide(interval, other_interval):

            return True

    return False


# helper function for memoization

def list_pair_to_surrogate(list_1, list_2):

    return str(list_1) + "|" + str(list_2)



def get_time_table(times_filename):

    times_file = open(times_filename)

    times = []

    for time in times_file:

        start_stop = time.strip().split()

        start = int(start_stop[0])
        stop  = int(start_stop[1])

        times.append((start, stop))

    return times


def get_max_recordable(times, selected, memo):

    # times - a list of time intervals (e.g. (1500, 1530))

    # selected - a list of all already selected time intervals

    if times == []:

        return 0

    elif memo.get(list_pair_to_surrogate(times, selected), None) != None:

        return memo[list_pair_to_surrogate(times, selected)]

    else:

        curr_time = times[0]

        selected_recurr_left  = copy.deepcopy(selected)
        
        selected_recurr_left.append(curr_time)
        
        selected_recurr_right = copy.deepcopy(selected)

        memo_key = list_pair_to_surrogate(times, selected)

        if not check_collision(curr_time, selected):

            left  = 1 + get_max_recordable(times[1:], selected_recurr_left, memo)
            right = get_max_recordable(times[1:], selected_recurr_right, memo)

            memo[memo_key] = max(left, right)

            return memo[memo_key]

        else:

            memo[memo_key] = get_max_recordable(times[1:], selected, memo)

            return memo[memo_key]

        
def get_time_table_bonus1(times_filename):

    times_file = open(times_filename)

    times = []

    for time in times_file:

        start_stop_show = time.strip().split()

        start = int(start_stop_show[0])
        stop  = int(start_stop_show[1])
        show  = str(start_stop_show[2])

        times.append((start, stop, show))

    return times


# helper function for bonus1

def list_from_str(list_str):

    res = []

    curr = ""

    make_interval = False

    for char in list_str:

        if char == "(":

            make_interval = True

        if char == ")":

            curr += char

            res.append(curr)

            curr = ""

            make_interval = False

            continue

        if make_interval:

            curr += char

    return res


def interval_str_to_interval(interval_str):

    # e.g. "(1530, 1600)" --> (1530, 1600)

    start_str = interval_str[1:interval_str.find(",")]
    stop_str  = interval_str[interval_str.find(", ")+2:len(interval_str)-1]

    start = int(start_str)
    stop  = int(stop_str)

    return (start, stop)


def bonus1(times_filename):

    # times - a list of time intervals (e.g. (1500, 1530))

    # selected - a list of all already selected time intervals


    # list of (start, stop) values

    time_table = get_time_table(times_filename)

    # list of (start, stop, show) values

    time_table_bonus1 = get_time_table_bonus1(times_filename)

    # a mapping of the form (start, stop) -> show

    showtime_map = {}

    for (start, stop, show) in time_table_bonus1:

        showtime_map[(start, stop)] = show

    # call standard 'max_recordable' function to fill in memo table

    memo = {}

    selected = []

    times = time_table

    test_val = get_max_recordable(times, selected, memo)

    print test_val

    # retrieve the times-selected pair of
    # lists which yielded the maximum value

    max_value = -1
    max_key   = ""

    for key in memo.keys():

        if memo[key] > max_value:

            max_value = memo[key]
            max_key   = key

    times_str    = max_key.split("|")[0]
    selected_str = max_key.split("|")[1]

    times_int_list    = list_from_str(times_str)
    selected_int_list = list_from_str(selected_str)

    times    = map(lambda x:interval_str_to_interval(x), times_int_list)
    selected = map(lambda x:interval_str_to_interval(x), selected_int_list)

    shows = []

    for interval in selected:

        shows.append(showtime_map[interval])

    #return shows
