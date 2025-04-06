import sys
input=sys.stdin.readline

s1=input().strip();s2=input().strip()
n1=len(s1);n2=len(s2)
dp=[[0]*(n2+1) for _ in range(n1+1)]

for i in range(1,n1+1):
  for j in range(1,n2+1):
    if s2[j-1]==s1[i-1]: dp[i][j]= dp[i-1][j-1]+1
    else: dp[i][j]= max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])