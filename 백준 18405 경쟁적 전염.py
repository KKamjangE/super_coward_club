import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split()) # 지도의 크기, 바이러스 개수

N_map = [list(map(int, input().split())) for _ in range(N)] # 시험관

S, X, Y = map(int, input().split()) # 시간, x좌표, y좌표

que = [] # 현재 퍼뜨려지는 바이러스들
next_virus = [] # 다음 시간에 퍼질 바이러스들

for i in range(N):
    for j in range(N):
        if N_map[i][j] != 0:
            heapq.heappush(que, (N_map[i][j], i, j)) # que에 초기 바이러스 위치 저장
          
dx = [1, -1, 0, 0] # x 좌표 탐색용
dy = [0, 0, 1, -1] # y 좌표 탐색용

count = 0 # 시간 counter

while count != S: # 할당된 시간이 끝나면 종료
    while que: # que가 빌 때까지
        virus, x, y = heapq.heappop(que) # 제일 낮은 바이러스 번호와 좌표 받기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: # 시험관안에 좌표라면
                if N_map[nx][ny] == 0: # 아직 바이러스가 없다면
                    N_map[nx][ny] = virus # 해당 영역 바이러스로 변경
                    next_virus.append((N_map[nx][ny], nx, ny)) # 변경된 영역 다음에 퍼질 바이러스에 추가
    
    count += 1 # 시간 +
    for _ in range(len(next_virus)):
        heapq.heappush(que, heapq.heappop(next_virus)) # 다음에 퍼질 바이러스들 que에 옮기기

print(N_map[X-1][Y-1]) # 해당 좌표에 어떤 바이러스가 있는지 출력