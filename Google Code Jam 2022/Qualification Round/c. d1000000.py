result = ""
number = int(input())
for x in range(number):
    limit = int(input())
    array = list(map(int, input().split()))
    counter = 1
    array.sort()
    highest = array[len(array)-1]
    for y in range(1,len(array)):
        if highest <= array[len(array)-1-y]:
            highest -= 1 
        else:
        	highest = array[len(array)-1-y]
        counter += 1
        if highest == 1:
            break
    result += f"Case #{str(x+1)}: {str(counter)}\n"
print(result[:-1])