import sys
input = sys.stdin.readline

n = int(input())
dp=[]

for _ in range(n):
    x=list(map(int,input().split()))
    x+=[0]*(n-len(x))
    dp.append(x)

for i in range(1,n):
        for j in range(i+1):
            dp[i][j]+=max(dp[i-1][j], dp[i-1][j-1])
            
print(max(dp[n-1]))
    