import sys
from collections import deque
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

def bfs(graph,r,visited):   
    visited[r]=True
    q=deque([r])
    while q:
      v=q.popleft()
      for i in graph[v]:
        if not visited[i]: 
          q.append(i)
          visited[i]=True

n=int(input())
m=int(input())
graph= [[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)            

bfs(graph,1,visited)
print(sum(visited[1:])-1)            