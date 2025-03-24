import sys
from collections import deque
q = deque()

for _ in range(int(sys.stdin.readline()) ):
    x = list(map(int, sys.stdin.readline().split()))
    match x[0]:
        case 1: q.append(x[1])
        case 2: q.appendleft(x[1])
        case 3: print(q.pop() if q else -1)    
        case 4: print(q.popleft() if q else -1)
        case 5: print(len(q))
        case 6: print(1 if not q else 0)
        case 7: print(q[-1] if q else -1)
        case 8: print(q[0] if q else -1)