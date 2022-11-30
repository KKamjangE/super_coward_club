import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chick_list = []
home_list = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            home_list.append((i, j))
        elif matrix[i][j] == 2:
            chick_list.append((i, j))
h_to_c = []

chick_comb = list(combinations(chick_list, m))
sum_list = []


for chick_list in chick_comb:
    h_to_c.clear()
    for home in home_list:
        min_d = 99
        hx, hy = home

        for chick in chick_list:
            cx, cy = chick
            distance = abs(cx - hx) + abs(cy-hy)
            if min_d > distance:
                min_d = distance
        h_to_c.append(min_d)
    sum_list.append(sum(h_to_c))
print(min(sum_list))