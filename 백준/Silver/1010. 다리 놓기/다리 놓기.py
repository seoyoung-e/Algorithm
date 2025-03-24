import math
import sys

m= int(sys.stdin.readline())
for _ in range(m):
    n,r = map(int, sys.stdin.readline().split())
    print(math.comb(n, r) if n >= r else math.comb(r,n))