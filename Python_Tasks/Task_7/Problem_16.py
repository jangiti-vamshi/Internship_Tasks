# 16 Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    res = []
    k = k % 26
    for char in s:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            res.append(new_char)
        elif 'A' <= char <= 'R' or 'A' <= char <= 'Z':
            if 'A' <= char <= 'Z':
                new_char = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
                res.append(new_char)
            else:
                res.append(char)
        else:
            res.append(char)
    return "".join(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
