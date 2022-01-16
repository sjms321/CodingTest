import sys

n = int(input())
num = []
for _ in range(n):
    #이게 input()보다 빠르다
    num.append(int(sys.stdin.readline())) 



num.sort()

for i in num:
    print(i)