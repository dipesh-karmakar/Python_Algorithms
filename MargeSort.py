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

This module will consolidate basic and advanced sorting algorithms
We will start with merge sort, later will extend to more complex algorithms
"""

################################################################################
#                                                                              #
# File : MargeSort.py                                                          #
#                                                                              #
# Desc: This file contains various merge sort algorithms implemented in Python #
#       Input is restricted to integers, individual object based               #
#       implementation is not in the scope of this document                    #
#                                                                              #
# Change log:                                                                  #
# ---------------------------------------------------------------------------- #
#   Date            Author                      Change Desc                    #
# ---------------------------------------------------------------------------- #
#   11/03/2018      Dipesh Karmakar             Initial file contains complete #
#                   dipesh.karmakar@gmail.com   merge sort v1 code             #
################################################################################


class MergeSort(object):
    """
    Made a class here to consolidate algorithms, will add more algorithms in future
    """

    def _sortlist(self, list_ds, first_list_start_index, second_list_start_index, last_index):
        """
        Merge two sorted lists
        1. Create an empty list called sorted list
        2. Traverse 2 lists and based on ascending/descending order,
           update the sorted list
        """
        # Create the empty list
        sorted_list_len = last_index - first_list_start_index + 1
        sorted_list = [0] * sorted_list_len
        s_l_index = 0
        f_index = first_list_start_index
        s_index = second_list_start_index
        sec_list_end = last_index + 1
        # Search the minimum of two input sorted list and
        # update the sorted list
        while (f_index != second_list_start_index) and (s_index != sec_list_end):
            if list_ds[f_index] <= list_ds[s_index]:
                sorted_list[s_l_index] = list_ds[f_index]
                s_l_index += 1
                f_index += 1
            else:
                sorted_list[s_l_index] = list_ds[s_index]
                s_l_index += 1
                s_index += 1

        # Copy the remaining sorted data to the sorted list as index
        # got exhausted in previous loop
        if f_index != second_list_start_index:
            for item in list_ds[f_index:second_list_start_index]:
                sorted_list[s_l_index] = item
                s_l_index += 1
        elif s_index != sec_list_end:
            for item in list_ds[s_index:sec_list_end]:
                sorted_list[s_l_index] = item
                s_l_index += 1

        f_index = first_list_start_index
        s_index = 0
        # Place the updated sorted list into the original list as
        # this is in-place sort
        while s_index < sorted_list_len:
            list_ds[f_index] = sorted_list[s_index]
            f_index += 1
            s_index += 1


    def mergesort_v1(self, list_ds):
        """
        Main merge sort algorithm version 1.0
        Instead of breaking the list in 2^n form i.e. conventional way,
        we are taking 1, 2, 4, 8 (2^4 starting from 1) pairs of data and
        merge them in to the original list
        """
        list_size = len(list_ds)
        list_size_rbone = list_size - 1
        element_power = 1
        # Loop in 1, 2, 4, 8 (2^4 starting from 1) fashion
        while element_power < list_size:
            fst_index = 0
            sec_index = fst_index + element_power
            lst_index = sec_index + element_power - 1
            # Separate two lists and pass it to '_sortlist' method
            # to merge them together
            while (sec_index < list_size) and (fst_index < list_size):
                if sec_index >= list_size:
                    sec_index = list_size_rbone
                    lst_index = list_size_rbone
                if lst_index >= list_size:
                    lst_index = list_size_rbone

                # Private method to merge two lists
                self._sortlist(list_ds, fst_index, sec_index, lst_index)

                # Update all index for next iteration
                fst_index = lst_index + 1
                sec_index = fst_index + element_power
                lst_index = sec_index + element_power - 1

                # Second list grows out of bound
                if sec_index > list_size_rbone:
                    break

            # Update the power in 2^n fashion
            element_power *= 2


    def islistsorted(self, list_ds):
        """
        A simple method, traverse through the list and checks
        whether the list is sorted or not
        """
        for index in range(0, len(list_ds) - 1):
            if list_ds[index] > list_ds[index + 1]:
                return False
        return True

# Unit Test code
# if __name__ == "__main__":
    # import random
    # import cProfile
    # SORT = MergeSort()
    # ORG_DATA_SET = [random.randint(0, 10000000) for x in range(0, 100000)]
    # cProfile.run("SORT.mergesort_v1(ORG_DATA_SET)")
    # print SORT.islistsorted(ORG_DATA_SET)
