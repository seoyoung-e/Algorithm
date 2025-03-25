import sys
input=sys.stdin.readline

n=int(input())
num= list(map(int,input().split()))
dp=[0]*n;dp[0]=num[0]

for i in range(1,n):
    #num[i]와 num[i]+dp[i-1] 결과를 비교해서 큰 수 업데이트
    dp[i]= max(num[i], num[i]+dp[i-1])
print(max(dp))
