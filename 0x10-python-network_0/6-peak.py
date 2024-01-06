#!/usr/bin/python3
""" finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """ func """

    if list_of_integers is None or list_of_integers == []:
        return None
    L = 0
    h = len(list_of_integers)
    md = ((h - L) // 2) + L
    md = int(md)
    if h == 1:
        return list_of_integers[0]
    if h == 2:
        return max(list_of_integers)
    if list_of_integers[md] >= list_of_integers[md - 1] and\
            list_of_integers[md] >= list_of_integers[md + 1]:
        return list_of_integers[md]
    if md > 0 and list_of_integers[md] < list_of_integers[md + 1]:
        return find_peak(list_of_integers[md:])
    if md > 0 and list_of_integers[md] < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
