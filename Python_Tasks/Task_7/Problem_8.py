# 8 Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

import math
import os
import random
import re
import sys

def gemstones(arr):
    common_chars = set(arr[0])
    for s in arr[1:]:
        common_chars.intersection_update(set(s))
    return len(common_chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
