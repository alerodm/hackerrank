"""
Given five positive integers, find the minimum and maximum values that can be 
calculated by summing exactly four of the  five integers. Then print the 
respective minimum and maximum values as a single line of two space-separated
long integers. 
"""

import itertools


def miniMaxSum(arr):
    sums = [sum(x) for x in itertools.combinations(arr, 4)]
    return (min(sums), max(sums))

def test_me():
    assert miniMaxSum([1,2,3,4,5]) == (10, 14)
