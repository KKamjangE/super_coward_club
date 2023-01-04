from collections import deque

import heapq

jobs = [[0, 3], [1, 9], [2, 6]]


def solution(jobs):
    ans = 0
    now = 0
    c = len(jobs)
    while jobs:
        heap = []
        for i, val in enumerate(jobs):
            a = val[0]
            b = val[1]
            heapq.heappush(heap, [abs(now - a) + b, a, b, i])
        x, y, z, i = heapq.heappop(heap)
        del jobs[i]
        ans += x
        now += z
    return ans // c


solution(jobs)
