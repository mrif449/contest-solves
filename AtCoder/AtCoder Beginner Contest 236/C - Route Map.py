a,b = map(int,input().split())
array1 = input().split()
array2 = input().split()
start = 0
end = 0
for x in range(len(array1)):
    if array1[start] == array2[end]:
        print("Yes")
        start+=1
        end+=1
    elif array1[start] != array2[end]:
        print("No")
        start+=1