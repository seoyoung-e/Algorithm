import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, m, n, matrix):
    q = [(x, y)]
    matrix[x][y] = 0 

    while q:
        x, y = q.pop(0)  # FIFO 방식으로 큐 처리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx, ny))

t = int(input())  # 테스트 케이스 수
for _ in range(t):
    # 배추밭 가로, 세로, 배추 개수
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)] 
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1 

    for a in range(m):
        for b in range(n):
            if matrix[a][b] == 1:
                bfs(a, b, m, n, matrix)
                cnt += 1  # 연결된 배추덩어리 ++

    print(cnt)
