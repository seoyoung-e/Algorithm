import sys
input=sys.stdin.readline
n=int(input())

from collections import Counter
x=list(map(int,sys.stdin.read().split())) 
cnt= Counter(x)

stack=[]
answer=[-1]*n #답

for i in range(n):
    while stack and cnt[x[stack[-1]]] < cnt[x[i]]: #기존 스택에 있는 마지막 애보다 cnt 더 많다면
        answer[stack.pop()]=x[i]
    stack.append(i)

print(*answer)