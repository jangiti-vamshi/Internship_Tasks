# 5 Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    return sum(1 for i in range(len(s) - 1) if s[i] == s[i + 1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
