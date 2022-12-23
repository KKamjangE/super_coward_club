import sys
input = sys.stdin.readline

N = int(input())

rgb_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]

for i in range(3):
    dp[0][i] = rgb_list[0][i]
    
for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][j+1]+rgb_list[i][j], dp[i-1][j+2]+rgb_list[i][j])
        if j == 1:
            dp[i][j] = min(dp[i-1][j-1]+rgb_list[i][j], dp[i-1][j+1]+rgb_list[i][j])
        if j == 2:
            dp[i][j] = min(dp[i-1][j-1]+rgb_list[i][j], dp[i-1][j-2]+rgb_list[i][j])
            
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))