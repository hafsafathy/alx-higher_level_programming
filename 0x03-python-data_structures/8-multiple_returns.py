#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        char = None
    else:
        char = sentence[0]
    return ((l, char))
