array = []
word = input()
a,b = map(int,input().split())
for x in word:
    array.append(x)
 
temp = array[a-1]
array[a-1] = array[b-1]
array[b-1] = temp
result = ""
for z in array:
    result += z
print(result)