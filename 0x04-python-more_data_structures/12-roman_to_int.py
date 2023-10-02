#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roms_lst = list(roman_string.upper())
    res = 0
    n = 0
    for i in roms_lst:
        if i in roms:
            res += roms[i]
            if roms[i] > n:
                res -= n * 2
            n = roms[i]
        else:
            return (0)
    return (res)
