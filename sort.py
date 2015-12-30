#
# sort.py
#

import random


test_input = [5, 3, 2, 1, 4]



#
# swap - primitive op.
#

def swap(List, i, j):

    temp    = List[i]
    List[i] = List[j]
    List[j] = temp





#
# Insertion Sort - O(n^2)
#
#
# NOTE: this function sorts
#       InpList in-place...
#

def insertsort(InpList):

    for i in range(0, len(InpList)):

        j = i

        while (j > 0) and (InpList[j] <= InpList[j-1]):

            swap(InpList, j, j-1)

            j = j - 1

    # no return statement: in-place sorting.





#
# Helper function (for selectsort)
#
#
# returns index of minimum element
# in list 'List', starting
# from index 'start'
#
#
# REQUIRES: 0 <= start <= len(List)
#

def indexOfMin(List, start):

    minIndex = start
    minElem  = List[start]

    for i in range(start, len(List)):

        if List[i] < minElem:

            minIndex = i
            minElem  = List[i]

    return minIndex



#
# Selection Sort - O(n^2)
#
# NOTE: This function sorts inpList in-place...
#

def selectsort(InpList):

    for i in range(0, len(InpList)):

        j = indexOfMin(InpList, i)
        
        swap(InpList, i, j)

    # no return statement: in-place sorting.





#
# merge - mergesort helper
#
#
# REQUIRES: L1 & L2 are sorted
#
# ENSURES: res contains the merged version of L1 with L2
#

def merge(L1, L2, res):

    if (len(L1) == 0):

        res.extend(L2)
    
    elif (len(L2) == 0):

        res.extend(L1)

    else:

        hd_L1 = L1[0]
        hd_L2 = L2[0]

        if (hd_L1 <= hd_L2):

            res.append(hd_L1)

            merge(L1[1:], L2, res)
        
        else:

            res.append(hd_L2)
            
            merge(L1, L2[1:], res)



#
# Mergesort - O(n*log(n))
#
#
# ENSURES: returns the sorted version of InpList
#

def mergesort(InpList):

    if len(InpList) <= 1:

        return InpList
    
    else:
        
        left  = InpList[:len(InpList)/2]
        right = InpList[len(InpList)/2:]
        
        res = []

        merge(mergesort(left), mergesort(right), res)

        return res



#
# Quicksort - O(n*log(n)) expected
#
#
# ENSURES: returns the sorted version of InpList
#

def quicksort(InpList):

    if (len(InpList) <= 1):

        return InpList

    else:

        pivot = random.sample(InpList, 1)[0]

        less    = filter(lambda x:x < pivot,  InpList)
        equal   = filter(lambda x:x == pivot, InpList)
        greater = filter(lambda x:x >  pivot, InpList)

        less_sorted  = quicksort(less)
        greater_sorted = quicksort(greater)

        res = less_sorted
        res.extend(equal)
        res.extend(greater_sorted)

        return res
