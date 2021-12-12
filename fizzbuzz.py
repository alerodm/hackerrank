#!/bin/python3

import math
import os
import random
import re
import sys


def fizzBuzz(n):
    for i in range(1, n+1):
        is_multiple_5 = n % 5 == 0
        is_multiple_3 = n % 3 == 0
        if is_multiple_5 and is_multiple_3:
            return "FizzBuzz"
        elif is_multiple_3:
            return "Fizz"
        elif is_multiple_5:
            return "Buzz"
        else:
            return n

if __name__ == '__main__':
    n = int(input().strip())
    fizzBuzz(n)


def test_me():
    assert fizzBuzz(15) == "FizzBuzz"
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(5) == "Buzz"
    assert fizzBuzz(4) == 4
