#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (C) 2018  Dipesh Karmakar

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You can receive a copy of the GNU General Public License from
http://www.gnu.org/

This module will consolidate basic and advanced search algorithms
We will start with simple binary search, later will extend to BST,
y-fast tries, fusion tree and continue
"""

################################################################################
#                                                                              #
# File : SearchAlgorithm.py                                                    #
#                                                                              #
# Desc: This file contains the binary search algorithm implemented in Python   #
#       Input is restricted to integers, individual object based               #
#       implementation is not in the scope of this document                    #
#                                                                              #
# Change log:                                                                  #
# ---------------------------------------------------------------------------- #
#   Date            Author                      Change Desc                    #
# ---------------------------------------------------------------------------- #
#   24/02/2018      Dipesh Karmakar             Initial file contains complete #
#                   dipesh.karmakar@gmail.com   binary search v1 code          #
#   06/03/2018          -||-                    Added b_search_v2 and          #
#                                               l_search_v1 functions          #
################################################################################


class SearchAlgorithm(object):
    """
    Made a class here to consolidate algorithms, will add more algorithms in future
    """
    def __init__(self):
        """ Basic CTOR, add proper code in future if necessary """
        self._binary_divider_const = 2
        # In future we can search in sub list OR portion of the list
        # using properly defined start index
        self._s_index = 0

    def b_search_v1(self, data_list, search_var):
        """
        Binary search version 1.0
        1. Input list must be sorted.
        2. Algorithm complexity is O(log n) in worst case
        3. Binary search compares the target value to the middle element
           of the array. If they are unequal, the half in which the target
           cannot holds good is eliminated and the search continues on the
           remaining half until it is successful.
           If the search ends with the remaining half being empty,
           the target is not in the array.
        """
        first_index = self._s_index
        last_index = len(data_list) - 1
        result_index = None
        # Continue the loop until first and last index crosses together
        while first_index <= last_index:
            # This code will check for all the left and right element of the
            # pivot and return in-case target found.
            # This will save few iterations
            if data_list[first_index] == search_var:
                result_index = first_index
                break
            if data_list[last_index] == search_var:
                result_index = last_index
                break

            # Find the mid position of the list
            pivot_index = (last_index + first_index) // self._binary_divider_const
            temp_val = data_list[pivot_index]
            # Compare equality
            if temp_val == search_var:
                result_index = pivot_index
                break
            elif temp_val < search_var:
                first_index = pivot_index + 1
            else:
                last_index = pivot_index - 1

        return result_index

    def b_search_v2(self, data_list, search_var, start_index=0, end_index=None):
        """
        Binary search version 2.0, using recursion
        1. Input list must be sorted.
        2. Algorithm complexity is O(log n) in worst case
        3. Binary search compares the target value to the middle element
           of the array. If they are unequal, the half in which the target
           cannot holds good is eliminated and the search continues on the
           remaining half until it is successful.
           If the search ends with the remaining half being empty,
           the target is not in the array. This logic repeats in a recursive
           function call fashion
        """
        if end_index is None:
            end_index = len(data_list) - 1
        if start_index > end_index:
            return None

        # This code will check for all the left and right element of the
        # sub-list and return in-case target found, this will save few iterations
        if data_list[start_index] == search_var:
            return start_index
        if data_list[end_index] == search_var:
            return end_index

        # No need of integer type cast, '//' will do the job, floor division
        mid_index = (start_index + end_index) // self._binary_divider_const
        # Compare equality
        if data_list[mid_index] == search_var:
            return mid_index
        elif data_list[mid_index] > search_var:
            return self.b_search_v2(data_list, search_var, start_index, (mid_index - 1))
        return self.b_search_v2(data_list, search_var, (mid_index + 1), end_index)

    def l_search_v1(self, data_list, search_var):
        """
        Linear search version 1.0, using recursion
        1. Input list may no be sorted, as this is a linear search
        2. Algorithm complexity is O(n) in worst case
        3. Linear search compares the target value to every element of the list,
           and return when found
        """
        ret_index = None
        for index in range(self._s_index, len(data_list)):
            if data_list[index] == search_var:
                ret_index = index
                break
        return ret_index


# Unit Test code
# if __name__ == "__main__":
    # DATA_POOL = [x for x in range(10000)]
    # SEARCH_ALGO_OBJ = SearchAlgorithm()
    # SEARCH_ALGO_OBJ.__binary_divider_const = 2
    # VAL = 4998
    # FINAL_RESULT_INDEX = None
    # import cProfile
    # """ Test for b_search_v1 """
    # cProfile.run("FINAL_RESULT_INDEX = SEARCH_ALGO_OBJ.b_search_v1(DATA_POOL, VAL)")
    # RESULT_STR = "Algo: b_search_v1 Value {} is found in index {}".format(VAL, FINAL_RESULT_INDEX)
    # """ Compatible print for Python 2.X and 3.X """
    # print (RESULT_STR)

    # """ Test for b_search_v2 """
    # cProfile.run("FINAL_RESULT_INDEX = SEARCH_ALGO_OBJ.b_search_v2(DATA_POOL, VAL)")
    # RESULT_STR = "Algo: b_search_v2 Value {} is found in index {}".format(VAL, FINAL_RESULT_INDEX)
    # """ Compatible print for Python 2.X and 3.X """
    # print (RESULT_STR)

    # """ Test for l_search_v1 """
    # cProfile.run("FINAL_RESULT_INDEX = SEARCH_ALGO_OBJ.l_search_v1(DATA_POOL, VAL)")
    # RESULT_STR = "Algo: l_search_v1 Value {} is found in index {}".format(VAL, FINAL_RESULT_INDEX)
    # """ Compatible print for Python 2.X and 3.X """
    # print (RESULT_STR)
