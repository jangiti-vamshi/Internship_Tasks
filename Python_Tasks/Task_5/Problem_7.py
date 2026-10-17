# 7 Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))

# Find the symmetric difference using the symmetric_difference() method or ^ operator
symmetric_diff = set_a.symmetric_difference(set_b)

# Print sorted results one per line
for num in sorted(symmetric_diff):
    print(num)
