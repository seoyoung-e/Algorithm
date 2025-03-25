import sys
input=sys.stdin.readline
import heapq
n=int(input())
h=[]

for _ in range(n):
    x=int(input())
    if x==0:print(heapq.heappop(h)[1] if h else 0)    
    elif x<0:  heapq.heappush(h, (-1*x,x))
    else: heapq.heappush(h, (x,x))