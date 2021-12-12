"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares
has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

    The length of the segment matches Ron's birth month, and,
    The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.
"""
def segmenter(arr, n):
    groups = []
    for i in range(len(arr)-n+1):
        groups.append(arr[i:i+n])
    return groups


def birthday(s, d, m):
    valid_segments = 0
    for segment in segmenter(s, m):
        if sum(segment) == d:
            valid_segments += 1
    return valid_segments


def test_me():
    assert birthday([1, 2, 1, 3, 2], 3, 2) == 2
    assert birthday([4], 4, 1) == 1