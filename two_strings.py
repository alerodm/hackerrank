# Given two strings, determine if they share a common substring. A substring 
# may be as small as one character. 

def twoStrings(s1, s2):
    return "YES" if set(s1).intersection(set(s2)) else "NO"


def test_me():
    assert twoStrings("hello", "world") == "YES"
