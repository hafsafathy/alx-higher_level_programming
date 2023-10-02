#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lst = list(a_dictionary.keys())
    lst.sort()
    for i in lst:
        print("{}: {}".format(i, a_dictionary.get(i)))
