import sys
import math
input = sys.stdin.readline

T = int(input())

def prime(N): # 소수인지 판별
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True


for _ in range(T): # 테스트 케이스 수 만큼 실행
    n = int(input())
    for j in range(n//2, n): # 받은 수에서 -
        if prime(j) and prime(n-j): # 두 수가 모두 소수이면
            print(n-j, j) # 출력
            break