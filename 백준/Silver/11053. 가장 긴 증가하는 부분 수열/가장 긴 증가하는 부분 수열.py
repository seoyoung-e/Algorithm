import sys
input = sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))

dp=[1]*(n)

for i in range(1,n):
    for j in range(i):
        if num[i]>num[j] and dp[i]<dp[j]+1: # 수가 증가했고, 이전 증가 부분 길이보다 현재 거가 크다면 업뎃
             dp[i]=dp[j]+1

print(max(dp))
