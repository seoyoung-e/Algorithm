import sys
input=sys.stdin.readline
sys.setrecursionlimit(1000000) 
from collections import deque

dfs1=[]
def dfs(i):
    dfs1.append(i)
    visited[i]=True
    for i in graph[i]:
        if not visited[i]: dfs(i)

bfs1=[]
def bfs(start):
    visited[start]=True
    bfs1.append(start)
    q=deque([start])
    while q:
        j=q.popleft()
        for i in graph[j]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
                bfs1.append(i)   
    
n,m,v= map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph=[sorted(h) for h in graph]
visited=[False]*(n+1)
dfs(v);print(*dfs1)

visited=[False]*(n+1)
bfs(v);print(*bfs1)