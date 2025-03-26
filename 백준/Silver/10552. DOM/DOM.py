import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(graph, visited, idx):
    if visited[idx]: return -1
    visited[idx]=True
    
    next_ch=graph[idx]
    if next_ch==-1: return 0 #더 이상 갈 채널 없음
    
    result=dfs(graph, visited, next_ch)
    if result==-1: return -1 #무한루프
    else: return result+1

n, m, p = map(int, input().split())
graph = [-1 for i in range(m + 1)] 
visited = [False for i in range(m + 1)] 

for i in range(1,n+1): 
    u, v = map(int, input().split()) #좋 싫
    if graph[v]== -1 : graph[v]=u #싫어하는 채널에서 좋아하는 채널로 이동하기 위함

print(dfs(graph, visited, p))