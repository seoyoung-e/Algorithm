import sys
input=sys.stdin.readline
import heapq
n=int(input())
h=[]

for _ in range(n):
    x=int(input())
    if not x: print(heapq.heappop(h) if h else 0)    
    else: heapq.heappush(h, x)