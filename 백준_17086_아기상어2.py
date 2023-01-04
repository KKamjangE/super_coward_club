import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, x, y):
    queue = deque([field[x][y], x, y])
    field_visit[x][y] = 1
    max = 0
    while queue:
        val, x_now, y_now = queue.popleft()
        if val == 0:
            field_visit.append(n)
            queue += graph[n] - set(field_visit)
    return field_visit


N, M = map(int, input().split())
field = []
field_visit = [[0 for _ in range(M)] for _ in range(N)]
print(field_visit)
for _ in range(N):
    field.append(list(map(int, input().split())))
