number= int(input())
 
for x in range (number):
    array = []
    string = input()
    for x in range(len(string)):
        if string[x] not in array:
            array.append(string[x])
    if len(array)>1: 
        def swap(c, i, j):
            c = list(c)
            c[i], c[j] = c[j], c[i]
            return ''.join(c)
        
        for y in range(len(string)):
            if string[0] != string[y]:
                new_var = swap(string, 0, y)
        print("YES")
        print(new_var)
        
    else:
        print("NO")