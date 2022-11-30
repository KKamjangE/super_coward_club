from heapq import heappush, heappop
def solution(food_times, k):

    # 주어진 초가 전체 음식을 먹는데 충분하다면 -1을 반환 
    if sum(food_times) <= k:
        return -1
    
    # 먹는데 걸리는 시간이 적은 음식을 먼저 다 먹어주어야 하므로 우선순위 큐를 사용해준다.
    q = []
    for i in range(len(food_times)):
        heappush(q, (food_times[i], i + 1))

    # 음식을 먹기 위해 사용한 시간
    sum_value = 0

    # 직전에 다 먹은 음식의 시간을 저장
    
    previous = 0 

    # 먹고 남은 음식의 수
    length = len(food_times)

    # 이전에 음식을 다 먹음으로써 감소한 시간을 다른 음식들에도 적용해 주어야한다. -> previous를 빼주면된다.
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 인덱스 순으로 다시 정렬해준다.
    result = sorted(q, key=lambda x : x[1])
    # '남은' 음식 중에서 몇 번째 음식인지 확인하며 출력
    return result[(k-sum_value) % length][1]



