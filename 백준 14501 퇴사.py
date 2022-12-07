import sys
input = sys.stdin.readline
import heapq

N = int(input())

dp = [0] * (N+1)
day_price =[]

for i in range(N):
    day, price = map(int, input().split())
    heapq.heappush(day_price, (day, price, i+1))

# print(day_price)

for _ in range(N):
    
    end_time, price, day = heapq.heappop(day_price)
    current_price = 0
    
    if day+end_time > N:
        continue
    
    current_price = sum(dp[day:end_time])
        
    if dp[day+end_time] < price and current_price < price:
        dp[day+end_time-1] += price
        
print(sum(dp))