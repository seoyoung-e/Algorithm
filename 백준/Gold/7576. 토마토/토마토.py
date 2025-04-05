import sys
from collections import deque

input=sys.stdin.readline
m,n=map(int, input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

q = deque([])
dx=[-1,1,0,0];dy=[0,0,-1,1]
ans=0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1: q.append([i,j]) #익은 토마토만 고르기
            
#bfs
while q:
    x,y=q.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny]= graph[x][y]+1
            q.append([nx,ny])
                
for i in graph:
    for j in i:
        if j==0: print(-1); exit(0)
    ans=max(ans,max(i))

print(ans-1)  #처음에 익은 토마토가 1로 표시되어 있으므로 빼주기    