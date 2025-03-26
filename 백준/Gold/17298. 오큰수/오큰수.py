import sys
input=sys.stdin.readline
n=int(input())
x = list(map(int,sys.stdin.read().split()))
stack=[]
answer=[-1]*n

for i in range(n):
    while stack and x[stack[-1]]<x[i]:
        answer[stack.pop()]=x[i]
    stack.append(i)

print(*answer)
