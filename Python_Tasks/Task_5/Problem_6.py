# 6 Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct_heights = set(array)
    avg = sum(distinct_heights) / len(distinct_heights)
    return round(avg, 3)
