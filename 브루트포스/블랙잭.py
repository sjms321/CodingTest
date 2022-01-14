

n, m = map(int,input().split())
arr = list(map(int,input().split()))
result = 0

for first in range(n):
    for second in range(first+1,n):
        for third in range(second+1,n):
            if arr[first] + arr[second] + arr[third]<=m and arr[first] + arr[second] + arr[third]>=result :
                result = arr[first] + arr[second] + arr[third]

             
print(result)


