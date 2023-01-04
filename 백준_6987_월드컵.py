import sys

input = sys.stdin.readline

result = []
for _ in range(4):
    team_list = list(map(int, input().split()))

    for i in range(0, 15, 3):
        target_win = team_list[i]
        target_draw = team_list[i + 1]
        target_lose = team_list[i + 2]
        visited = [0] * 6

        if target_win > 0:
            for j in range(i + 5, 18, 3):
                if team_list[i] == 0:
                    break
                if (team_list[j] > 0) and (visited[j // 3] == 0):
                    team_list[j] -= 1
                    team_list[i] -= 1
            visited[j // 3] = 1

        if target_draw > 0:
            for j in range((i + 1) + 3, 18, 3):
                if team_list[i + 1] == 0:
                    break
                if (team_list[j] > 0) and (visited[j // 3] == 0):
                    team_list[j] -= 1
                    team_list[i + 1] -= 1
            visited[j // 3] = 1

        if target_lose > 0:
            for j in range((i + 2) + 1, 18, 3):
                if team_list[i + 2] == 0:
                    break
                if (team_list[j] > 0) and (visited[j // 3] == 0):
                    team_list[j] -= 1
                    team_list[i + 2] -= 1
            visited[j // 3] = 1

    if len(set(team_list)) != 1:
        result.append(0)
    else:
        result.append(1)

print(*result, sep=" ")
