# Problem Name : Validating the Phone Number
# HackerRank : https://www.hackerrank.com/challenges/validating-the-phone-number/problem


import re

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        number = input().strip()

        if re.fullmatch(r'[789]\d{9}', number):
            print("YES")
        else:
            print("NO")
