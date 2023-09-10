#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if not sentence:
        return (l, None)
    else:
        return (l, sentence[0])
