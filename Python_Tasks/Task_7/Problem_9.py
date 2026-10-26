# 9 Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

import sys

def beautifulBinaryString(b):
    return b.count('010')

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    b = sys.stdin.readline().strip()
    result = beautifulBinaryString(b)
    print(result)
