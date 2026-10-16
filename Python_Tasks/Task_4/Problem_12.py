# Problem Name : Introduction to Sets
# HackerRank : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    array=set(array)
    avg=(sum(array))/(len(array))
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
