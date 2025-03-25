import sys
input= sys.stdin.readline

n=int(input())
num=list(map(int,input().split()))
num_rev=num[::-1]

dp=[1]*(n);dp_rev=[1]*(n)

for i in range(n):
    for j in range(i):
        if num[i]>num[j]:dp[i]=max(dp[i], dp[j] + 1)
        if num_rev[i]>num_rev[j]: dp_rev[i] = max(dp_rev[i], dp_rev[j] + 1)      

                    
for i in range(0,n-1): dp[i]+= dp_rev[n-1-i]-1
print(max(dp))

            