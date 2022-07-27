from math import ceil
import sys


class ListForBinarySearch(object):
    def __init__(self, number_array):
        self.lst = number_array
        self.target = None
        self.max = sys.maxsize
        self.min = -sys.maxsize - 1
        
    def get_occurence_range_for(self, target):
        self.target = target
        min_index = self.find_index(0, len(self.lst) - 1, min, self.max)
        max_index = self.find_index(0, len(self.lst) - 1, max, self.min)

        return (min_index, max_index)

    def find_index(self, first, last, func, extreme):
        if self.lst[first] > self.target:
            return extreme
        if self.lst[last] < self.target:
            return extreme
        if last - first == 0:   # this call checks if there is only one list element remaining
            return first if self.lst[first] == self.target else extreme     # if the last element is target return index, otherwise return extreme

        sublist_length = last - first + 1
        middle_index = ceil(sublist_length / 2) - 1 + first

        return func(self.find_index(first, middle_index, func, extreme), self.find_index(middle_index + 1, last, func, extreme))
