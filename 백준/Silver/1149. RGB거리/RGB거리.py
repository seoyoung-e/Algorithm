import sys
input=sys.stdin.readline
n=int(input())
color=[list(map(int,input().split()))  for _ in range(n)]

for i in range(1,n):
  for j in range(3):
    color[i][j] += min(color[i-1][(j+1)%3], color[i-1][(j+2)%3])
print(min(color[-1]))