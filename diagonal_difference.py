"""
Given a square matrix, calculate the absolute difference between the sums
of its diagonals.
"""


def diagonalDifference(arr):
    sum_diag1 = 0
    sum_diag2 = 0
    for i, row in enumerate(arr):
        sum_diag1 += row[i]
        sum_diag2 += row[0-i-1]
    return abs(sum_diag1 - sum_diag2)


def test_me():
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    assert diagonalDifference(arr) == 15
