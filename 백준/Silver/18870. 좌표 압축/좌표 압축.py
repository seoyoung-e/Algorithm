import sys
input=sys.stdin.readline
n=int(input())

item=list(map(int, input().split()))
x=sorted(set(item))

a=dict()
for idx,i in enumerate(x): a[i]=idx

for j in item: print(a[j],end=" ")