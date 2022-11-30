import sys
input = sys.stdin.readline

N, M = map(int, input().split())

road_list = [list(map(int, input().split())) for _ in range(N)]
cnt_list = []

# step = [[0, 1], [0, -1], [1, 0], [-1, 0]] # R, L, U, D

for i in range (N):
    for j in range(N):
        target = road_list[i][j]
        if target != 2:
            continue
        else:
            cnt = 0
            for k in range(-1, 2):
                for y in range(-1, 2):
                    ni = i+k
                    nj = j+y
                    if ni < 0 or ni > N-1:
                        continue
                    if nj < 0 or nj > N-1:
                        continue
                    point = road_list[ni][nj]
                    print(ni, nj)

                    if point == 1:
                        cnt += 1
            cnt_list.append([cnt, i, j])

cnt_list.sort(key=lambda x:-x[0])

print(cnt_list)
