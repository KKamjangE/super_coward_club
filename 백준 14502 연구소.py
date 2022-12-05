import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque()
virus = deque()

for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            que.append((i, j))

print(que)

while que:
    current = que.popleft()
    print(current)
    x, y = current
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < M:
            if map[nx][ny] == 0:
                map[nx][ny] = 2
                que.append((nx, ny))
                
# visit = [[False] * N for _ in range(M)]

print(map)