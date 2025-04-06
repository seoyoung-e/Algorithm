import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    p,c,w=map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))
    
def dfs(start,wei): #시작 노드, 이전까지 가중치
    for i,w in graph[start]:
        if dist[i]==-1 : 
            dist[i]=w+wei
            dfs(i,wei+w)
            
dist=[-1]*(n+1)
dist[1]=0 #1번 노드 시작
dfs(1,0) 

node=dist.index(max(dist))
dist=[-1]*(n+1)
dist[node]=0 
dfs(node,0) 
print(max(dist))