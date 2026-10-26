# 1 Set .symmetric_difference() Operation
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

n = int(input())
set_a = set(map(int, input().split()))
m = int(input())
set_b = set(map(int, input().split()))

print(len(set_a.symmetric_difference(set_b)))
