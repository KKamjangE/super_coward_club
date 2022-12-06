import sys
import math
input = sys.stdin.readline

N, K = map(int, input().split())

def eratos(): # 소수 구하기 기본형
    nums = [True] * (N + 1)
    for i in range(2, int(math.sqrt(N))+1): # 소수인지 확인
        if nums[i] == True:
            for j in range(i+i, N, i): # 배수 지우기
                nums[j] = False
    print([i for i in range(2, N) if nums[i] == True])

count = 0

err = False

nums = [True] * (N+1)
for i in range(2, len(nums) + 1):
    if err:
        break
    for j in range(i, N+1, i):
        if nums[j] == True:
            nums[j] = False
            count += 1
            if count == K:
                print(j)
                err = True
                break