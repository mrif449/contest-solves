number = int(input())
for x in range(number):
    length = int(input())
    string = input()
    array = []
    for y in range(len(string)):
        if string[y] not in array:
            array.append(string[y])
    array.sort()
    array2 = array[::-1]
    string2 = ""
    array3 = []
    for z in string:
        index = array.index(z)
        array3.append(index)
    for a in array3:
        string2+= array2[a]
    print(string2)