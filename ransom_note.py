"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be 
traced back to him through his handwriting. He found a magazine and wants to 
know if he can cut out whole words from it and use them to create an untraceable
replica of his ransom note. The words in his note are case-sensitive and he 
must use only whole words available in the magazine. He cannot use substrings 
or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes 
if he can replicate his ransom note exactly using whole words from the 
magazine; otherwise, print No.
"""

import collections


def checkMagazine(magazine: list, note: list) -> str:
    magazine_word_count = collections.Counter(magazine)
    note_word_count = collections.Counter(note)
    word_diff = note_word_count - magazine_word_count
    return "Yes" if len(word_diff.keys()) == 0 else "No"


def test_me():
    assert checkMagazine("give me one grand today night", "give one grand today") == "Yes"
    assert checkMagazine("two times three is not four", "two times two is four") == "No"
    assert checkMagazine("ive got a lovely bunch of coconuts", "ive got some coconuts") == "No"
