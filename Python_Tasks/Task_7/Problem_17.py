# 17 Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first_num = int(s[:i])
        current = first_num
        built = str(current)
        while len(built) < n:
            current += 1
            built += str(current)
        if built == s:
            print(f"YES {first_num}")
            return
    print("NO")

if __name__ == '__main__':
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        q = int(input_data[0])
        for i in range(1, q + 1):
            separateNumbers(input_data[i])
