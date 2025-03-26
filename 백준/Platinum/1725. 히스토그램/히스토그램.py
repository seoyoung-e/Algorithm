import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int, sys.stdin.read().splitlines()))

stack = []
max_v = 0
for i in range(n): #커서처럼 각 블록 가장 왼쪽 꼭짓점 좌표
    idx = i
    while stack and stack[-1][1] > x[i]:
        idx, height = stack.pop()
        rst = (i-idx) * height
        max_v = max(max_v, rst)
    stack.append([idx, x[i]])
    
#전체가 동일한 높이일 경우
while stack:
    idx, height = stack.pop()
    rst = (n - idx) * height
    max_v = max(max_v, rst)

print(max_v)