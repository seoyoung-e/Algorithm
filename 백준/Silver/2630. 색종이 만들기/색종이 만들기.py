def div(y,x,n):
  color=paper[y][x]
  for i in range(y,y+n):
    for j in range(x,x+n):
      if color != paper[i][j]: #분할 중 색 다르면
        m=n//2 
        #더 작은 영역 4개로 나눠서 보기
        div(y,x,m) #2사분면
        div(y,x+m,m)  #1
        div(y+m,x,m) #3
        div(y+m,x+m,m) #4
        return
      
  if color==0: result[0]+=1 #흰색일때
  else: result[1] += 1 #파란색

n=int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
result=[0,0] #자른 흰색/파란색 종이
div(0,0,n)
print(result[0],'\n',result[1],sep='')
