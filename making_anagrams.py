"""
A student is taking a cryptography class and has found anagrams to be very 
useful. Two strings are anagrams of each other if the first string's letters 
can be rearranged to form the second string. In other words, both strings 
must contain the same exact letters in the same exact frequency. For example, 
bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings.
The encryption is dependent on the minimum number of character deletions 
required to make the two strings anagrams. Determine this number. 
Given two strings, and , that may or may not be of the same length,
determine the minimum number of character deletions required to make and 
anagrams. Any characters can be deleted from either of the strings. 
"""

from collections import Counter


def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    diff_counter = counter_a.copy()
    diff_counter.subtract(counter_b)
    return sum(abs(x) for x in diff_counter.values())


def test_me():
    assert makeAnagram("cde", "abc") == 4
    assert makeAnagram("cde", "dcf") == 2
    assert makeAnagram("foobar", "barfoox") == 1
    assert makeAnagram("bacdc", "dcbad") == 2
    assert makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke") == 30
    assert makeAnagram("showman", "woman") == 2
