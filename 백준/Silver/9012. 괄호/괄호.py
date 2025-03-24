import sys
n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().strip()
    answer=0
    
    for i in a:
        if i=="(" : answer+=1
        else:answer-=1
            
        if answer<0: print("NO"); break
    
    
    else:  # break 없이 정상적으로 끝난 경우
        if answer == 0:
            print("YES")
        else:
            print("NO")
 