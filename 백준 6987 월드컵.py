import sys
input = sys.stdin.readline

def dfs(index):
    global win, lose, tie, tie_cnt
    
    if index >= 17:
        return
    
    win += score[index]
    tie += score[index+1]
    lose += score[index+2]

    if score[index+1] > 0:
        tie_cnt += 1
    
    dfs(index+3)

for _ in range(4):
    score = list(map(int, input().split()))
    win = 0 # 승
    lose = 0 # 패
    tie = 0 # 무승부
    tie_cnt = 0 # 무승부인 나라 수
    tie_err = False # 무승부 체크
    dfs(0)

    if tie > 0 and tie_cnt <= 1:
        tie_err = True
        
    if win != lose or 30 != (win+lose+tie) or tie_err:
        print(0)
    else:
        print(1)