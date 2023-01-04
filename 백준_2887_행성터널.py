import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def sol(depth, start, cost):
    global m
    if depth == N:
        m = min(m, cost)
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            sol(
                depth + 1,
                i,
                cost
                + min(
                    abs(point[start][0] - point[i][0]),
                    abs(point[start][1] - point[i][1]),
                    abs(point[start][2] - point[i][2]),
                ),
            )
            visit[i] = 0


N = int(input())
point = []
visit = [0 for _ in range(N)]
m = 1e9
for _ in range(N):
    x, y, z = map(int, input().split())
    point.append([x, y, z])

sol(0, 0, 0)
print(m)
