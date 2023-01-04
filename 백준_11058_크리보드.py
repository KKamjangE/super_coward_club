num =int(input())
data=[i for i in range(num+1)]

for i in range(7,num+1):
    data[i]=max(data[i-3]*2, data[i-4]*3, data[i-5]*4)

print(data)