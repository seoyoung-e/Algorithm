import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)
n,e= map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w))
    graph[v].append((u, w))
    
v1,v2=map(int, input().split())


def dijkstra(start,end):
    dist = [INF] * (n+1) 
    q=[]
    heapq.heappush(q,(0,start))
    dist[start]=0
    
    while q:
        d, now = heapq.heappop(q) #최단 거리 노드 정보 꺼내기
        if dist[now]< d : continue 
    
        for next_node, weight in graph[now]:
            cost = d + weight #시작노드부터 next_code까지의 거리 
            if cost < dist[next_node]: 
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    return dist[end] 

r1= dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,n)
r2= dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,n)
print(-1 if r1>=INF and r2>=INF else min(r1,r2))


