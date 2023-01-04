import sys

input = sys.stdin.readline


def sol(i):
    global ans
    global sum
    sum += time_money[i][1]
    ans = max(ans, sum)
    if i + time_money[i][0] <= N:
        posible = i + time_money[i][0]
    else:
        return
    sol(posible)

    return


N = int(input())
time_money = [0]
ans = 0


for _ in range(N):
    time, money = map(int, input().split())
    time_money.append([time, money])

for i in range(1, N):
    sum = 0
    if i + time_money[i][0] < N:
        sol(i)

print(ans)
