import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
s, x, y = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            q.append((i, j, 0, matrix[i][j]))
            visited[i][j] = True


q.sort(key=lambda x: x[3])

def bfs():

    newq = deque(q)
    while newq:
        cx, cy, day, virus = newq.popleft()

        if day == s:
            return 

        for dir in range(4):
            nx = dx[dir] + cx
            ny = dy[dir] + cy
            nday = day + 1
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = virus
                    visited[nx][ny] = True

                    newq.append((nx, ny, nday, virus)) 


bfs()
print(matrix[x-1][y-1])
