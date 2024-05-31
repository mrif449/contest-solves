answer = ""
result = ""
limit = int(input())
for x in range(limit):
    number = int(input())
    array = []
    for y in range(1,number+1):
        array.append(y)
    start = 0
    if len(array)%2 == 0:
            for x in range(0,int((len(array))-2),2):
                temp = array[x]
                array[x] = array[x+1]
                array[x+1] = temp
    else:
            for x in range(1,int((len(array))-2),2):
                start = 1
                temp = array[x]
                array[x] = array[x+1]
                array[x+1] = temp                
    for z in array:
        result += str(z)+" "
    result += "\n"
result = result[:-1]
print(result)