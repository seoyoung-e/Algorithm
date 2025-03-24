import sys
n=int(sys.stdin.readline().strip())
stack=[]
commands = sys.stdin.read().splitlines()

for xx in commands:
    xx=xx.split()
    if len(xx)==1:
        x = int(xx[0])
        if x==2:print(stack.pop() if stack else -1)
        elif x==3: print(len(stack))
        elif x==4: print(0 if stack else 1)
        elif x==5: print(stack[-1] if stack else -1)
    
    else: stack.append(int(xx[1]))
       
    