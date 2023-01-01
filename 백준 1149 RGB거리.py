import sys
input = sys.stdin.readline

N = int(input()) # 집의 크기 N * N

rgb_list = [list(map(int, input().split())) for _ in range(N)] # 집의 비용들

dp = [[0] * 3 for _ in range(N)] # dp 테이블

for i in range(3): # dp 테이블에 y번 집 대입
    dp[0][i] = rgb_list[0][i]
    
for i in range(1, N):
    for j in range(3): # 색상 3개 고정
        # 색상이 겹치지 않아야 한다
        # j번과 다른 색상의 다음 집과 더해서 비용이 더 작은것을 dp 테이블에 저장한다
        if j == 0: # 0번째 집
            dp[i][j] = min(dp[i-1][j+1]+rgb_list[i][j], dp[i-1][j+2]+rgb_list[i][j])
        if j == 1: # 1번째 집
            dp[i][j] = min(dp[i-1][j-1]+rgb_list[i][j], dp[i-1][j+1]+rgb_list[i][j])
        if j == 2: # 2번째 집
            dp[i][j] = min(dp[i-1][j-1]+rgb_list[i][j], dp[i-1][j-2]+rgb_list[i][j])
            
# dp 테이블의 마지막 줄에서 제일 낮은 값을 출력한다
print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))