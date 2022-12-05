# 매 초마다 번호가 낮은 종류의 바이러스 먼저 증식
# 바이러스가 존재한다면 다른 바이러스 x
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
virus_map = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

lst = []
for i in range(N):
    for j in range(N):
        if virus_map[i][j] != 0:
            lst.append((virus_map[i][j], i, j, 0))

lst.sort()
q = deque(lst)
def bfs():
    while q:
        virus_num, x, y, second = q.popleft()
    
        if second == S:
            return virus_map[X-1][Y-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 만약 바이러스가 존재한다면 다른 바이러스 x
                if virus_map[nx][ny] == 0:
                    virus_map[nx][ny] = virus_num
                    q.append((virus_num, nx, ny, second + 1))
                
    return virus_map[X-1][Y-1]

print(bfs())