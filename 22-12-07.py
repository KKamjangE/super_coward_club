# import sys
# input = sys.stdin.readline

# N = int(input())
# n_list = []
# result_list = []
# for _ in range(N):
#     T, P = map(int, input().split())
#     n_list.append((T,P))


# def test(idx: int, n_list: list):
#     global result

#     if (idx > N-1):
#         return
    
#     t, p = n_list[idx]

#     if (t > N-idx):
#         return result
#     else:
#         result += p
#         test(idx+t, n_list)


# for i in range(N):
#     result = 0
#     test(i, n_list)
#     result_list.append(result)
    

# print(max(result_list))


N = int(input())
work_pay = [list(map(int, input().split())) for _ in range(N)]
max_pay = [0] * N

for i in range(N - 1, -1, -1):
    day = work_pay[i][0]
    pay = work_pay[i][1]
    if day > N - i:
        if i != N - 1:
            max_pay[i] = max_pay[i + 1]
        continue
    elif i == N - 1:
        max_pay[i] = pay
    elif i + day == N:
        max_pay[i] = max(pay, max_pay[i + 1])
    else:
        max_pay[i] = max(pay + max_pay[i + day], max_pay[i + 1])
print(max_pay)