number = int(input())
array = list(map(int, input().split()))

highest = array[0]
for x in array:
    if x > highest:
        highest = x
new = [0]*(highest+10)
high = new[0]
result = 2
for y in range(2,highest+1):
    for z in array:
        if z%y == 0:
            new[y] += 1
    if new[y]>= high:
        high = new[y]
        result = y
print(result)