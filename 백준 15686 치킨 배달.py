import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = []

def dfs(x, y):
    visit[x][y] = True
    if city[x][y] == 2:
        heapq.heappush(q, abs(x-city_x)+abs(y,city_y))
        return
    if 0 <= x <= N and 0 <= y <= N:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx <= N and 0 <= ny <= N:
                if visit[nx][ny] == False:
                    dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if city[i][j] != 1:
            continue

        visit = [[False] * N for _ in range(N)]
        city_x, city_y = i, j
        dfs(i, j)
            
print(city)
print(visit)