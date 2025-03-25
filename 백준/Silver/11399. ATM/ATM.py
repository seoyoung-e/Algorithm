import sys
input=sys.stdin.readline

n=int(input())
items= list(map(int,sys.stdin.readline().split())) 
items.sort()
sum=0
for idx,v in enumerate(items):
    sum+= v*(n-idx)
print(sum)