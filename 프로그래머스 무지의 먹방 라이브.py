import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1 반환
    if sum(food_times) <= k:
        return -1
    
    q = [] # q 배열 생성
    for i in range(len(food_times)): # q에 push
        heapq.heappush(q, (food_times[i], i+1)) # (음식 먹는 시간, 음식 순번)
        
    sum_time = 0 # 음식을 먹는데 사용한 시간
    prav_time = 0 # 직전에 다먹은 음식 시간
    food_count = len(food_times) # 남은 음식의 개수
    
    while sum_time + ((q[0][0] - prav_time) * food_count) <= k: #  
        now_time = heapq.heappop(q)[0] # q에서 먹는 시간이 제일 적은 음식의 시간
        sum_time += (now_time - prav_time) * food_count # (현재 음식 먹는 시간 - 이전에 먹었던 음식들 시간) * 남은 음식 개수
        food_count -= 1 # 음식 하나를 다 먹음
        prav_time = now_time # 이전에 먹은 음식 시간 갱신
        
    ans = sorted(q, key=lambda x:x[1]) # 남은 음식을 순번에 따라 오름차순 정렬
    
    return ans[(k - sum_time) % food_count][1] # (k - 지금까지 음식을 먹는데 사용한 총 시간) % 남아있는 음식의 개수
        
food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))