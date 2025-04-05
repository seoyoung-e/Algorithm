import sys
input=sys.stdin.readline

n,m= map(int, input().split())
item= list(map(int,input().split()))
item.sort()
low, high= 1,item[-1]

while low <= high:
  mid=(low+high)//2
  total=0
  for i in item:
    if i>=mid: total+= i-mid
  
  if total>=m: low= mid+1
  else: high=mid-1
print(high)