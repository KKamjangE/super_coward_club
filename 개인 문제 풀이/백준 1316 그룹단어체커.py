import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for _ in range(N):
    word = input().strip()
    group = True
    for i in range(len(word)):
        if not group:
            break
        check = True
        count = word.count(word[i])
        for j in range(i, len(word)):
            if word[i] == word[j] and not check:
                group = False
            if word[i] != word[j]:
                check = False
                
    if group:
        ans += 1
        
print(ans)
