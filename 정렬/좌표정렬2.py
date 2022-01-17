import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
arr = []

for _ in range(N):
    x, y = map(int, read().split())
    arr.append([x, y])

arr.sort(key=lambda x:(x[1], x[0]))

for x, y in arr:
    print(x, y)