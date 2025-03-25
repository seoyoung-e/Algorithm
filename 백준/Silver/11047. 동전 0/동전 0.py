import sys
input=sys.stdin.readline
n,result= map(int, input().split())

items=list(map(int, sys.stdin.read().splitlines()))
items=items[::-1]

cnt=0
for i in items:
  if result//i>0:
    cnt+= result//i; result= result%i
print(cnt)