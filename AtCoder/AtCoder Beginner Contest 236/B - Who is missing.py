number = int(input())
index = number+1
array = list(map(int, input().split()))
array.sort()
new = [0]*index
for x in array:
    new[x] += 1
for y in range(len(new)):
    if new[y] == 3:
        result = y
print(result)