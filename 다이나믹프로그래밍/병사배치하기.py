n =int(input())
array = list(map(int,input().split()))


#순서를 뒤집어서 최장증가부분수열 문제로 변환
array.reverse()

dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))


