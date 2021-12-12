"""
You are given a string containing characters A and B only. Your task is to 
change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
"""


def alternatingCharacters(s):
    delete_count = 0
    for i, chr in enumerate(s[:-1]):
        if chr == s[i+1]:
            delete_count +=1
    return delete_count


def test_me():
    assert alternatingCharacters("AABAAB") == 2
    assert alternatingCharacters("AAAA") == 3
    assert alternatingCharacters("BBBBB") == 4
    assert alternatingCharacters("ABABABAB") == 0
    assert alternatingCharacters("BABABA") == 0
    assert alternatingCharacters("AAABBB") == 4
    assert alternatingCharacters("") == 0
