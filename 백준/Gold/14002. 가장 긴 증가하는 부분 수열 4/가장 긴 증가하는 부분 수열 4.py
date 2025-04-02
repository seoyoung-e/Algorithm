import sys
input = sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))

dp=[1]*(n)
path=[-1]*(n+1)

for i in range(1,n):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]+1:
             dp[i]=dp[j]+1
             path[i]=j

i=dp.index(max(dp))
print(dp[i])

from collections import deque
ans=deque()
while i>-1:
  ans.append(num[i])
  i=path[i]

while ans: print(ans.pop(),end=' ')