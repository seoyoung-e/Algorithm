import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq
n, m = map(int, input().split())
k = int(input())
INF = int(1e9)


dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w)) 


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #시작노드로 가기 위한 최단 경로 0으로 넣고 시작
    dist[start]=0
    
    while q:
        d, now = heapq.heappop(q) #최단 거리 노드 정보 꺼내기
        if dist[now]< d : continue 
        for j in graph[now]:
            cost=d + j[1] 
            if cost < dist[j[0]]: 
                dist[j[0]]= cost
                heapq.heappush(q, (cost, j[0]))
                   
            
dijkstra(k)
for i in range(1, n+1):
    print("INF" if dist[i]==INF else dist[i])