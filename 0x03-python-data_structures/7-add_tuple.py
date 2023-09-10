#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = len(tuple_a)
    l_b = len(tuple_b)
    ntup = ()
    for i in range(2):
        if i >= l_a:
            a = 0
        else:
            a = tuple_a[i]
        if i >= l_b:
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            ntup = (a + b)
        else:
            ntup = (ntup, a + b)
    return (ntup)
