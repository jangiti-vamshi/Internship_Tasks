# Problem Name : Find the Runner-Up Score!
# HackerRank : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_arr=list(set(arr))
    new_arr.sort(reverse=True)
    print(new_arr[1])
