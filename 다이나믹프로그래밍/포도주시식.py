n=int(input())
podojoo=[0]*10000
for i in range(n):
  podojoo[i]=int(input())

dp=[0]*10000
dp[0]=podojoo[0]
dp[1]=podojoo[0]+podojoo[1]
dp[2]=max(podojoo[2]+podojoo[0], podojoo[2]+podojoo[1], dp[1])
for i in range(3,n):
  dp[i]=max(podojoo[i]+dp[i-2], podojoo[i]+podojoo[i-1]+dp[i-3], dp[i-1])

print(max(dp))