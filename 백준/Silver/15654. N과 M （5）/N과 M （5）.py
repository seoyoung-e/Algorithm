import sys
input=sys.stdin.readline
n,m=map(int, input().split())
item=list(map(int,input().split())) 
item.sort()

from itertools import permutations
for i in permutations(item,m):print(*i)