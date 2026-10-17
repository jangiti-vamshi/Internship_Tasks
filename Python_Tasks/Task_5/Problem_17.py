# 17 No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

def solve():
    n, m = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
  
    happiness = sum((i in set_a) - (i in set_b) for i in arr)
    
    print(happiness)

if __name__ == '__main__':
    solve()
