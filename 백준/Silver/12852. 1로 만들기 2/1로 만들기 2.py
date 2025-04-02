import sys
input=sys.stdin.readline

n=int(input())
dp=[0 for _ in range(n+1)]
path=[0 for _ in range(n+1)]

for i in range(2,n+1):
  #1빼는 걸 기본 선택으로
  path[i]=i-1
  dp[i]=dp[i-1]+1
  if i%2==0 and dp[i] > dp[i//2]+1:
    dp[i]=dp[i//2]+1
    path[i]=i//2
  if i%3==0 and dp[i]>dp[i//3]+1: 
    dp[i]=dp[i//3]+1
    path[i]=i//3

answer=[]
while n>0:
  answer.append(n)
  n=path[n]

print(dp[-1])
print(*answer)
    