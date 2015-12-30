
#
# sortedinsert.py - DATA STRUCTURE
#
# Defines a 'sortlist' data structure
# supporting insert/delete operations,
# while maintaining a list in sorted-order
#

import sort


class SortList(object):


    sortlist = None
    cmp      = None



    # create a new 'empty' sortlist,
    # with the given comparison function, cmp
    
    def __init__(self, cmp):

        self.sortlist = []
        self.cmp      = cmp

        return None



    # return string representation of sortlist

    def __str__(self):

        return str(self.sortlist)



    # insert a new element - O(n) complexity

    def insert(self, elem):

        if (len(self.sortlist) == 0):

            self.sortlist = [elem]

        else:

            # cmp(x, y) == -1 if x < y
            # cmp(x, y) == 0  if x = y
            # cmp(x, y) == 1  if x > y

            self.sortlist.append(elem)

            j = len(self.sortlist) - 1

            while (j > 0):

                left  = self.sortlist[j-1]
                right = self.sortlist[j]

                if (self.cmp(left, right) >= 0):

                    sort.swap(self.sortlist, j, j-1)

                    j = j - 1
                    
                else:

                    break



    # delete an element from the sortlist - O(n) complexity

    def delete(self, i):

        if not (0 <= i <= len(self.sortlist) - 1):

            raise RuntimeError, "Error: Index out-of-range"

        j = i

        while (j + 1 < len(self.sortlist)):

            sort.swap(self.sortlist, j, j + 1)

            j = j + 1

        self.sortlist = self.sortlist[:len(self.sortlist)-1]



    # convert from a Python list to sortlist

    def fromList(self, std_list):   # better to have an overloaded __init__

        curr = std_list
        
        curr.sort()

        self.sortlist = curr



    # convert from sortlist to a Python list

    def toList(self):

        return self.sortlist
