#!/bin/python

def flatten(l):
    """Flattens nested lists into a single list.

    :param list l: a list that potentially contains other lists.
    :rtype: list"""
    ret=[]
    for i in l:
        if isinstance(i, list): ret+=flatten(i)
        else: ret.append(i)
    return ret
