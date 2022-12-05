import sys
from collections import deque
import copy


n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# 너비 우선 탐색으로 바이러스를 퍼트린다.
# 바이러스를 퍼트린 후, 몇개인지 센다.
def spread_virus():
    q = deque()
    temp_map = copy.deepcopy(matrix)
    cnt = 0

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                q.append((i, j))

    while q:
        cx, cy = q.popleft()

        for dir in range(4):
            nx = dx[dir] + cx
            ny = dy[dir] + cy

            if 0 <= nx < n and 0 <= ny < m:
                if temp_map[nx][ny] == 0:
                    temp_map[nx][ny] = 2
                    q.append((nx, ny))


    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 0:
                cnt += 1

    res.append(cnt)

# 벽을 세우는 메서드
# 벽을 3개를 세웠다면 바이러스를 퍼트리고 안전영역을 센다.
# 결과를 리스트에 넣고 제일 먼저 세웠던 벽을 지우고 다시 벽을 세운다.
def wall(cnt):
    if cnt == 3:
        spread_virus()
        return
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(cnt+1)
                matrix[i][j] = 0
wall(0)

print(max(res))