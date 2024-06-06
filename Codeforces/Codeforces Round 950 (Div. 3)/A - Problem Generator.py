number = int(input())
for x in range(number):
    n,m = map(int,input().split())
    string = input()
    counter = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    for y in string:
        if y.lower() == "a":
            a += 1
        elif y.lower() == "b":
            b += 1
        elif y.lower() == "c":
            c += 1
        elif y.lower() == "d":
            d += 1
        elif y.lower() == "e":
            e += 1
        elif y.lower() == "f":
            f += 1
        elif y.lower() == "g":
            g += 1
    if a < m:
        counter += (m-a)
    if b < m:
        counter += (m-b)
    if c < m:
        counter += (m-c)
    if d < m:
        counter += (m-d)
    if e < m:
        counter += (m-e)
    if f < m:
        counter += (m-f)
    if g < m:
        counter += (m-g)
    print(counter)