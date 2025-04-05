import sys
input=sys.stdin.readline
n=int(input())
graph= [[] for _ in range(n+1)]

for _ in range(n-1):
  a,b=map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


from collections import deque
visited = [0]*(n+1)
q=deque([1]) 

while q:
  now=q.popleft() #탐색할 노드
  for i in graph[now]: #자식 찾기
    if visited[i] ==0 : 
      visited[i]=now #부모 노드 넣기
      q.append(i)

print('\n'.join(map(str, visited[2:])))