def dfs(graph,r,visited):
    global t
    visited[r]=True
    cnt[r]=t
    t+=1
    for i in graph[r]:
        if not visited[i]: dfs(graph,i,visited)
                        
import sys
sys.setrecursionlimit(1000000)
input=sys.stdin.readline

n,e,r= map(int,input().split())
graph= [[] for _ in range(n+1)]
visited=[False]*(n+1)
cnt=[0 for _ in range(n+1)] #노드 방문 순서 저장 
t=1

for _ in range(e):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in range(1, n + 1):
    graph[i].sort(reverse=True)

dfs(graph,r,visited)
for i in range(1,n+1):
    print(cnt[i])