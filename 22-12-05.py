import sys

input = sys.stdin.readline

N, K = map(int, input().split())

n_list = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

target_list = [(X,Y)]

virus_list = []
for i in range(S):
    for j in range(4):
        x, y = target_list[i]
        nx = x + dx[j]
        ny = y + dy[j]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        print("x, y",x, y)
        print("nx, ny", nx, ny)
        target_list.append((nx,ny))

        target = n_list[nx][ny]
        
        if target != 0:
            virus_list.append(target)
    print("===")
print(virus_list)