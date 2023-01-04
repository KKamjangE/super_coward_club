import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
switch = []
result = 0
for i in range(N):
    a = list(map(int, input().split()))
    switch.append(a[1:])

combination = list(itertools.combinations(switch, N - 1))
for ele in combination:
    ans = list(set())
    for i in ele:
        ans.append(i)
    if len(ans) == M:
        result = 1
        break

print(result)
