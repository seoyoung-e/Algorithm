while True:
    a= input() #sys.stdin.readline().strip()
    stack=[]
    
    if a == ".": break
        
    for i in a:
         if i in "[(": stack.append(i)
         elif i == ']':
            if stack and stack[-1]=='[' : stack.pop()
            else: stack.append(i); break
         elif i == ')':
            if stack and stack[-1]=='(' : stack.pop()
            else: stack.append(i);break
    
    print('yes' if len(stack)==0 else 'no')