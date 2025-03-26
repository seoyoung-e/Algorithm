import sys
input=sys.stdin.readline
n=int(input())
x1,x2=map(int, input().split())

rel=int(input())
graph= [[] for _ in range(n+1)]

for _ in range(rel):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False for _ in range(n+1)]
cnt=0

def dfs(graph, visited, idx):
    global cnt
    if idx==x2: return cnt
    visited[idx]=True
  
    for i in graph[idx]:
      if not visited[i]:
        result= dfs(graph, visited,i)
        if result != -1: return result+1
    return -1 #다 훑어봐도 안 나올 경우


print(dfs(graph, visited, x1))