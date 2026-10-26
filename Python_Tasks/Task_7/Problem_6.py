# 6 Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem


import math
import os
import random
import re
import sys

def pangrams(s):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    input_set = set(s.lower())
    if alphabet_set.issubset(input_set):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
