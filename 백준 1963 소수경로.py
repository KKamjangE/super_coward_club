import sys, math
input = sys.stdin.readline

T = int(input())

arr = [True] * 10001

for i in range(2, int(math.sqrt(10001))):
    if arr[i] == True:
        j = 2
        for j in range(i+i, 10001, i):
            arr[j] = False
    print([i for i in range(2, 10001) if arr[i] == True])

for _ in range(T):
    a, b = map(int, input().split())
    