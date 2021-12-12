"""
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of 
input strings. Return an array of the results.
"""
import collections


def matchingStrings(strings, queries):
    results = []
    c = collections.Counter(strings)
    for q in queries:
        results.append(c[q])
    return results
