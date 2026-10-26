# 4 Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

import math
import os
import random
import re
import sys

def funnyString(s):
    rev = s[::-1]
    n = len(s)
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i-1])):
            return "Not Funny"
    return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for _ in range(q):
        s = input()
        result = funnyString(s)
        fptr.write(result + '\n')
    fptr.close()
