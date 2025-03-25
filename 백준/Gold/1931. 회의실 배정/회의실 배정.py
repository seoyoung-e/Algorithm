import sys
input=sys.stdin.readline

n=int(input())
items=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
items.sort(key=lambda x:(x[1], x[0])) #빨리 끝나는 순 > 이른 회의 순

end=0; cnt=0
for new_start,new_end in items:
    if end<=new_start: 
        cnt+=1 
        end=new_end
print(cnt)
    