number = int(input())
for x in range(number):
    integer = (input())
    counter = 0
    age = 0
    ahe2 = 0
    array = []
    for y in integer:
        array.append(int(y))
    for z in range(1,len(array)):
        if (array[z-1] == 1 and array[z] == 0) or (array[z-1] == 0 and array[z] == 1 and ahe2==1):
            counter += 1
        if array[z-1] == 0 and array[z] == 1:
            ahe2 = 1
    print(counter+1)