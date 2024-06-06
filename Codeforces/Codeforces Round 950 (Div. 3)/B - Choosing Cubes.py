
number = int(input())
for x in range(number):
    n,f,k = map(int,input().split())
    array = list(map(int, input().split()))
    array.sort()
    array.reverse()
    fav = array[f-1]
    for y in range(k):
        array.pop(0)
    print(fav)
    if fav not in array:
        print("Yes")
    else:
        if f<=k:
            print("Maybe")
        else:
            print("No")
