# 1 Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    arr.sort(reverse=True)
    print(arr[1])
