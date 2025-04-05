import sys
from collections import deque

input=sys.stdin.readline
n,m=map(int, input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,1,0,0];dy=[0,0,-1,1]
q = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j]==2: q.append([i,j]) #목표지점 찾기
             
while q:
    x,y=q.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny]= graph[x][y]+1
            q.append([nx,ny])

#목표 지점 2+거리니까 2씩 다 빼기            
#갈 수 있는데 도달할 수 없는 경우 1일거니까 2빼면 -1, 0은 그대로            
xx=[[n if n == 0 else n - 2 for n in i] for i in graph]
for i in xx: print(*i)
    
    