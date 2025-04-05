import sys
input=sys.stdin.readline

n,m= map(int,input().split())
item=list(map(int,input().split())) 

#누적합 구하기
ans=[0] ; x=0
for i in range(n):
    x+=item[i]
    ans.append(x)
      
for _ in range(m):
    a,b= map(int,input().split())
    print(ans[b]-ans[a-1])
