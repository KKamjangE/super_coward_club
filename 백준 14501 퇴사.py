import sys
input = sys.stdin.readline

N = int(input()) # 퇴사일

dp = [0] * (N+1) # dp 테이블 생성
work = [list(map(int, input().split())) for _ in range(N)] # work에 time, price 배열로 저장

for day in range(N-1, -1, -1): # 날짜 역순으로
    time = work[day][0] # 현재 work time가져오기
    
    if day + time <= N: # 현재 날짜 + time이 총 퇴사일보다 크지 않을 경우
        price = work[day][1] # 현재 work price 가져오기
        # 전날까지의 금액과 (현재 날짜 + work time) + price 비교해서 대입
        dp[day] = max(dp[day + 1], dp[day + time] + price)
        
    else: # 퇴사일을 넘어간다면
        dp[day] = dp[day + 1] # 전날까지의 금액으로 대입
        
print(dp[0]) # 마지막까지 합산된 금액 출력