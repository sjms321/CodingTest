N=int(input())
X = list(map(int,input().split()))
X.sort()
print(X)
count = int(0)
for i in X:
    if N > i :
        N = int(N)-i
        count +=1
    else :
        break

print(count)