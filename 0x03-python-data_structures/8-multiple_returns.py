#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if (l == 0):
        ntup = (l, None)
    else:
        ntup = (l, sentence[0])
    return (ntup)
