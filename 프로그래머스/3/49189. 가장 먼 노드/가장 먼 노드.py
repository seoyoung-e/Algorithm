import heapq

def solution(n, edge):
    graph = [[] for _ in range(n+1)] 
    for a, b in edge:
        graph[a].append((b, 1))  
        graph[b].append((a, 1))  

    def dijkstra(start, n, graph):
        INF = int(1e9)  
        dist = [INF] * (n+1)
        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0  

        while q:
            d, now = heapq.heappop(q)  
            if dist[now] < d: continue
            for neighbor, weight in graph[now]:  
                cost = d + weight
                if cost < dist[neighbor]: 
                    dist[neighbor] = cost
                    heapq.heappush(q, (cost, neighbor))
        return dist

    distances = dijkstra(1, n, graph)
    return distances.count(max(i for i in distances[1:]))
 