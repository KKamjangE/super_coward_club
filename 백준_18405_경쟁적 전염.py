import sys

input = sys.stdin.readline


def sol(now_x, now_y, val):
    if now_x - 1 >= 0:
        if die_map[now_x - 1][now_y] == 0:
            die_map[now_x - 1][now_y] = val
            visited[now_x - 1][now_y] = 0
    if now_x + 1 < x:
        if die_map[now_x + 1][now_y] == 0:
            die_map[now_x + 1][now_y] = val
            visited[now_x + 1][now_y] = 0
    if now_y - 1 >= 0:
        if die_map[now_x][now_y - 1] == 0:
            die_map[now_x][now_y - 1] = val
            visited[now_x][now_y - 1] = 0
    if now_y + 1 < x:
        if die_map[now_x][now_y + 1] == 0:
            die_map[now_x][now_y + 1] = val
            visited[now_x][now_y + 1] = 0


x, y = map(int, input().split())
die_map = [[0] for _ in range(x)]
visited = [[1 for _ in range(x)] for _ in range(x)]

for i in range(x):
    die_map[i] = list(map(int, input().split()))
s, ans_x, ans_y = map(int, input().split())

for _ in range(s):
    if die_map[ans_x - 1][ans_y - 1] != 0:
        break
    for w in range(x):
        for z in range(x):
            if die_map[w][z] != 0 and visited[w][z] == 1:
                visited[w][z] = 0
                sol(w, z, die_map[w][z])
    visited = [[1 for _ in range(x)] for _ in range(x)]
if die_map[ans_x - 1][ans_y - 1] == 0:
    print("0")
else:
    print(die_map[ans_x - 1][ans_y - 1])
