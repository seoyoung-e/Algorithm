import sys
input=sys.stdin.readline

n,m= map(int,input().split())
items=[list(map(int, input().split())) for _ in range(n)]

dp=  [[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1): #각 물건
    w,v= items[i-1]
    for j in range(m+1): #무게 점점 증가
        if w > j : dp[i][j] = dp[i-1][j] #현재 아이템 못 넣는 경우
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
print(max(dp[n]))