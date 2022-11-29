def solution(food_times, k):
    index = 0
    for _ in range(k):
        
        if index == len(food_times):
            index = 0
            
        if food_times[index] == 0:
            tmp = index
            while True:
                index += 1
                
                if food_times[index] > 0:
                    break

                if index == tmp:
                    break

                if index >= len(food_times):
                    index = 0
                
        food_times[index] -= 1
        
        index += 1
        
    return index + 1
        
food_times = [3, 1, 2]
k = 5

print(solution(food_times, k))