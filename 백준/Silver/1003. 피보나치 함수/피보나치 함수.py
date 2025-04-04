import sys
sys.setrecursionlimit(10000000)
input=sys.stdin.readline

dp = [(1, 0), (0, 1)] #(0 호출 수, 1 호출 수)
for i in range(2,41) : #n은 0~40
    zero = dp[i - 1][0] + dp[i - 2][0]
    one=dp[i - 1][1] + dp[i - 2][1]
    dp.append((zero,one))

n=int(input())
items= [int(sys.stdin.readline()) for _ in range(n)]

for m in items:print(*dp[m])