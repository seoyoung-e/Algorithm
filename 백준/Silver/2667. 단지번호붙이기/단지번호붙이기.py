import sys
input = sys.stdin.readline
from collections import deque

def bfs(graph,a,b,n):
    q=deque([(a, b)])
    graph[a][b]=0
    danji=1
    
    while q:
        x,y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                danji +=1
    return danji

dx=[-1,1,0,0]; dy=[0,0,-1,1]
n=int(input()) #n*n 격자
graph=[list(map(int, list(input().strip()))) for _ in range(n)] 
cnt = 0
h=[]

for a in range(n):
    for b in range(n):
        if graph[a][b]==1:
            h.append(bfs(graph,a,b,n))
            cnt+=1

print(cnt)
for x in sorted(h): print(x)