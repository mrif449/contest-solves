result = ""
number = int(input())
for x in range(number):
    limit = int(input())
    string = input().split()
    counter = 0
    array = []
    for a in string:
        array.append(int(a))
    if array[0] <= (array[limit-1]):
        highest = array[0]
    else:
        highest = (array[limit-1])
    start = 0
    end = limit-1
    for y in range(limit):
        if array[start] <= (array[end]) and (array[start])>=highest:
            highest = (array[start])
            counter += 1
        elif (array[end]) < (array[start]) and (array[end])>=highest:
            highest = (array[end])
            counter += 1
            end -= 1
            start-=1
        elif (array[end]) < (array[start]) and (array[end])< highest:
            end-=1
            start-=1
        start += 1
    result += f"Case #{x+1}: {str(counter)}\n"
print(result[:-1])