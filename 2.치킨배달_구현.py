import sys

input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))  # 이후 반복문을 돌면서, 각 인자에 리스트 추가

# dx = [0,0,-1,1] # 상하좌우
# dy = [-1,1,0,0]
for i in city:
    for j in i:
        print(city[i][j])
        if city[i][j] == 2:
            bfs()
            if city[i][j] == 1:
                ##주변 거리중 가장 작은 거리
                [i1 - i2]
            ##거리를 다구한다.

##거리를 다구하면 sort를 하여 구현하고
##오름차순으로 정렬한다.
## m개만 추출하여 sum한 값을 프린트한다 .


print(city[2][1])

print(city)

visited = [False] * N


def bfs(city, v, visited):
    ###큐구현을 위해 deque 라이브러리를 사용한다.
    queue = deque([v])
    ##현재 노드를 방문처리한다.
    visited[v] = True

    while queue:

        now = queue.popleft()
        ##탐색 순서 출력
        print(now, end=" ")
        for i in graph[now]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
