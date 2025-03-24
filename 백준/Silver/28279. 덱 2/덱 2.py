import sys
from collections import deque

n = int(sys.stdin.readline())  # 일관성 유지: input() → sys.stdin.readline()
q = deque()

for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))

    if len(x) > 1:
        num = x[1]
        if x[0] == 2:  # 🔹 올바르게 정수 비교 수행
            q.appendleft(num)
        else:
            q.append(num)
    else:
        num = x[0]
        if num == 3:
            print(q.pop() if q else -1)
        elif num == 4:
            print(q.popleft() if q else -1)
        elif num == 5:
            print(len(q))
        elif num == 6:
            print(1 if not q else 0)
        elif num == 7:
            print(q[-1] if q else -1)
        else:
            print(q[0] if q else -1)
