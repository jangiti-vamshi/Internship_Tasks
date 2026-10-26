# 13 Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())
    
    if len(counts) == 1:
        return "YES"
    
    if len(counts) == 2:
        c1, c2 = list(counts.keys())
        f1, f2 = counts[c1], counts[c2]
        
        if (c1 == 1 and f1 == 1) or (c2 == 1 and f2 == 1):
            return "YES"
        
        if (abs(c1 - c2) == 1) and (f1 == 1 or f2 == 1):
            if (c1 > c2 and f1 == 1) or (c2 > c1 and f2 == 1):
                return "YES"
                
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
