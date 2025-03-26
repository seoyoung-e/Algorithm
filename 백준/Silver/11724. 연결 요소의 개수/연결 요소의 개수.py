from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, start, visited):
    visited[start]=True
    q=deque([start])
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                
                
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
cnt=0
visited = [False] * (n+1)
for i in range(1,n+1):
     if not visited[i]:
            bfs(graph, i, visited)
            cnt+=1
            
print(cnt)
                
                
                
                
                
                
                
                