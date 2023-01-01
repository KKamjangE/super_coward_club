import sys
input = sys.stdin.readline

N = int(input())

count = 0 # N과 비교해서 dfs를 끝내기 위한 비교 값

def dfs(a, b):
    global count
    if count == N: # N과 같다면 a를 출력하고 dfs 종료
        print(a)
        return
    
    count += 1
    
    dfs(b, a + b)

dfs(0, 1)