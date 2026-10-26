# 10 CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem



import math
import os
import random
import re
import sys

def camelcase(s):
    return sum(1 for c in s if c.isupper()) + 1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
