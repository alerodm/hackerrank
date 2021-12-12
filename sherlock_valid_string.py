"""
Sherlock considers a string to be valid if all characters of the string appear 
the same number of times. It is also valid if he can remove just 1 character at 
1 index in the string, and the remaining characters will occur the same number 
of times. Given a string, determine if it is valid. If so, return YES,
otherwise return NO.
"""

from collections import Counter


def isValid(s):
    count_by_char = Counter(s)  # abbac -> {'a': 2, 'b': 2, 'c': 1}
    count_by_occurrence_num = Counter(count_by_char.values())  # {2: 2, 1: 1}
    count_by_occ_uniq_values = set(count_by_occurrence_num.keys())  # {1,2}
    
    if len(count_by_occ_uniq_values) == 1:
        return "YES"
    elif len(count_by_occ_uniq_values) == 2:
        max_count = max(count_by_occ_uniq_values)
        min_count = min(count_by_occ_uniq_values)
        # valid case if there's only one char with the biggest occurence, and the diff with the smallest one is 1
        if count_by_occurrence_num[max_count] == 1 and max_count - min_count == 1:
            return "YES"
        # valid case if there's only one char with the smallest occurence, and that occurrence is only 1
        if count_by_occurrence_num[min_count] == 1 and min_count == 1:
            return "YES" 
    return "NO"  


def test_me():
    assert isValid("abc") == "YES"
    assert isValid("abcc") == "YES"
    assert isValid("aabbcd") == "NO"
    assert isValid("abbac") == "YES"
    assert isValid("aabbccddeefghi") == "NO"
    assert isValid("abcdefghhgfedecba") == "YES"
