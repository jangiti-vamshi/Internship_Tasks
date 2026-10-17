# 20 Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        d = deque(map(int, input().split()))
        
        possible = True
        last_block = float('inf')
        
        while d:
            if d[0] >= d[-1]:
                current = d.popleft()
            else:
                current = d.pop()
                
            if current <= last_block:
                last_block = current
            else:
                possible = False
                break
                
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()
