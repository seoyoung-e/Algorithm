import sys
input = sys.stdin.readline
from collections import deque

def bfs(a,b):
    q=deque([(a, b)])
    while q:
        x,y= q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))
    return graph[n-1][m-1]

dx=[-1,1,0,0]; dy=[0,0,-1,1]
n,m=map(int,input().split())
graph=[list(map(int, list(input().strip()))) for _ in range(n)] 
print(bfs(0,0))