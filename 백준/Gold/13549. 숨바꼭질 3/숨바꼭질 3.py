import sys
input=sys.stdin.readline
n,k=map(int,input().split())

from collections import deque
limit=100001
visited=[0]*limit

def bfs():
    q=deque([(n,0)])
    visited[n]=1
    
    while q:
        x, time =q.popleft()
        if x==k: print(time); break
        
        jump=2*x; go=x+1; back=x-1
        
        if 0<= jump<limit and visited[jump]==0:
            q.append((jump,time))
            visited[jump]=1
        if 0<= back<limit and visited[back]==0:
            q.append((back,time+1))
            visited[back]=1
        if 0<= go<limit and visited[go]==0:
            q.append((go,time+1))
            visited[go]=1
        
bfs()