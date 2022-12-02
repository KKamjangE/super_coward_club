import sys

input = sys.stdin.readline

def sol()

Row, Col = list(map(int, input().split()))
main_list = [0 for _ in range(Row)]

for i in range(Row):
    main_list[i] = input().split()

print(main_list)

#브루트포스 문제여서 처음에 푸는 방법을 생각은 났으나 문제에 규칙이 있지 않을까 해서 찾아보다 풀지 못했다.