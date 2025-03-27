from collections import deque
def bfs(graph,r,visited):
    global t
    visited[r]=True
    cnt[r]=t;t+=1
    q=deque([r])
    while q:
      v=q.popleft()
      for i in graph[v]:
        if not visited[i]: 
          q.append(i)
          visited[i]=True
          cnt[i]=t;t+=1

import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,e,r= map(int,input().split())
graph= [[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=[0 for _ in range(n+1)] 
t=1

for _ in range(e):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort(reverse=True)

bfs(graph,r,visited)
for i in range(1,n+1):print(cnt[i])