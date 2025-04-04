import sys
input= sys.stdin.readline

n=int(input())
item=list(map(int, sys.stdin.read().splitlines()))
num=max(item)

dp=[0]*(num+1)
dp[1]=1;dp[2]=2;dp[3]=4
for i in range(4,num+1):
    dp[i]= dp[i-1]+dp[i-2]+dp[i-3]

for i in item:
    print(dp[i])