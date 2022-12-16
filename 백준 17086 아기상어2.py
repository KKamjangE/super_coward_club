import sys
input = sys.stdin.readline
N, M = map(int, input().split())

map_arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

ans = 0
find = False

def dfs(x, y, cnt):
    global find
    
    if find:
        return
    
    visit[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if map_arr[nx][ny] == 0 and not visit[nx][ny]:
                dfs(nx, ny, cnt+1)
            elif map_arr == 1:
                find = True
                ans = max(ans, cnt+1)
                return

for i in range(N):
    for j in range(M):
        if map_arr[i][j] == 0:
            visit = [[False] * M for _ in range(N)]
            find = False
            dfs(i, j, 0)
            
print(ans)