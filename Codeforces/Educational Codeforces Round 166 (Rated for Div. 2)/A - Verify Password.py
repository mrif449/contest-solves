number = int(input())
for x in range(number):
    length = int(input())
    password = input()
    string = ""
    wrong = 0
    array = []
    for y in password:
        if y.isupper():
            wrong += 1
        array.append(y)
    array.sort()
    for z in array:
        string += z
    if password != string:
        wrong += 1
    if wrong >= 1:
        print("NO")
    else: print("YES")