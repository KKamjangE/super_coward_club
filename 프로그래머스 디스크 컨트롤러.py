import heapq

jobs = [[0,3],[1,9],[2,6]]

def solution(jobs):
    que = []
    
    for i in range(len(jobs)):
        heapq.heappush(que, (jobs[i][1], jobs[i][0]))
        
    last, answer = heapq.heappop(que)
    
    while que:
        job_time, job_start = heapq.heappop(que)
        answer += (last - job_start) + job_time
        last += job_time
        
    return answer//3

print(solution(jobs))