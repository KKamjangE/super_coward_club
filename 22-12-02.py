import sys
input = sys.stdin.readline

N, M = map(int, input().split())

road_list = [list(map(int, input().split())) for _ in range(N)]
virus_list = []
wall_list = []

for i in range (N):
    for j in range(M):
        key = road_list[i][j]
        if key == 2:
            virus_list.append((i,j))
        elif key == 1:
            wall_list.append((i,j))

print(virus_list)
print(wall_list)
