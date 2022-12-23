import sys
input = sys.stdin.readline

N = int(input())

home = [list(map(int, input().split())) for _ in range(N)]


print(home)