import sys

input = sys.stdin.readline


def sol(x, y):
    x1, x2 = x[0], x[1]
    y1, y2 = y[0], y[1]
    if y == [N, N]:
        ans += 1
        return
    if x1 == y1:
        if y2 < N - 1 and not load_map[y1][y2 + 1]:
            sol(y, [y2, y2 + 1])
            if y1 < N - 1:
                if not load_map[y1 + 1][y2] and not load_map[y1 + 1][y2 + 1]:
                    sol(y, [y2 + 1, y2 + 1])
    if x1 != y1:
        if y1 < N - 1 and not load_map[y1+1][y2]:
            sol(y,[y1,y1+1])
            if y2<N-1:
                if not load_map[y1 + 1][y2] and not load_map[y1 + 1][y2 + 1]:
                    sol(y, [y2 + 1, y2 + 1])

    return


N = int(input())
load_map = []
ans = 0
# [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    load_map.append(list(map(int, input().split())))

sol([0, 0], [0, 1])
print(ans)
