import sys
input = sys.stdin.readline

s = set()
for _ in range(int(input())):
    item = list(input().split())
    if len(item) == 1:
        if item[0] == "all":
            s = set(i for i in range(1, 21))
        else:
            s = set()
    else:
        a, b = item[0], int(item[1])
        if a == "add":
            s.add(b)
        elif a == "remove":
            s.discard(b)  
        elif a == "check":
            print(1 if b in s else 0)
        elif a == "toggle":
            if b in s:
                s.remove(b)
            else:
                s.add(b)
    
        
        
        