"""
A string is said to be a special string if either of two conditions is met:

    All of the characters are the same, e.g. aaa.
    All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those 
criteria. Given a string, determine how many special substrings can be formed 
from it. 
"""
import itertools


def count_criteria1_matches(s):
    count = 0
    same_char_groups = ["".join(y) for x,y in itertools.groupby(s)]  # "aabc" -> ("aa", "b", "c") 
    for group in same_char_groups:
        count += (len(group) * (len(group) + 1)) // 2  # partial sum shortcut
    return count


def count_criteria2_matches(s):
    count = 0
    for i in range(1, len(s)-1):
        # discard cases from the first criteria
        if s[i] == s[i-1] or s[i] == s[i+1]:
            continue
        # count when chars to the sides of the current position match
        target_char = s[i-1]
        for x in range(1, min(i, len(s)-i-1) + 1):
            if target_char == s[i+x] and target_char == s[i-x]:
                count += 1
            else:
                break
    return count


def substrCount(n, s):
    criteria1_matches = count_criteria1_matches(s)
    criteria2_matches = count_criteria2_matches(s)
    return criteria1_matches + criteria2_matches
    

def test_me():
    assert substrCount(8, "mnonopoo") == 12
    assert substrCount(5, "asasd") == 7
    assert substrCount(7, "abcbaba") == 10
    assert substrCount(4, "aaaa") == 10

    with open('special_string_again_long_input.txt') as f:
        assert substrCount(627182, f.read()) == 753395
