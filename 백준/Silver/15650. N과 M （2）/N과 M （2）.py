import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())

item=[i for i in range(1,n+1)]
for i in combinations(item, m): print(*i)


