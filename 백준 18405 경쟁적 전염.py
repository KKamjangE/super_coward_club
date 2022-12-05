import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

N_map = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

que = []
next_virus = []

for i in range(N):
    for j in range(N):
        if N_map[i][j] != 0:
            heapq.heappush(que, (N_map[i][j], i, j))
          
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

while count != S:
    while que:
        virus, x, y = heapq.heappop(que)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if N_map[nx][ny] == 0:
                    N_map[nx][ny] = virus
                    next_virus.append((N_map[nx][ny], nx, ny))
    
    count += 1
    for _ in range(len(next_virus)):
        heapq.heappush(que, heapq.heappop(next_virus))

print(N_map[X-1][Y-1])