number = int(input())
for x in range(number):
    a,b,c,d = map(int,input().split())
    array1 = [a,b]
    array1.sort()
    array2 = [c,d]
    array2.sort()
    if array1[0] < array2[0]:
        a = array1[0]
        b = array1[1]
        c = array2[0]
        d = array2[1]
    else:
        c = array1[0]
        d = array1[1]
        a = array2[0]
        b = array2[1]
    
    if (a<c and c<b) and  (d>b or d<a):
        print("YES")
    else: print("NO")