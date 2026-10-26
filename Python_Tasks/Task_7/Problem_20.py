# 20 Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

import math
import os
import random
import re
import sys


def superReducedString(s):
    res = []
    for char in s:
        if res and res[-1] == char:
            res.pop()
        else:
            res.append(char)
    return "".join(res) if res else "Empty String"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    s = input()
    result = superReducedString(s)
    fptr.write(result + "\n")
    fptr.close()
