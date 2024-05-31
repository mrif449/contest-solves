result = ""
case = int(input())
for x in range(case):
    total,change = map(int,input().split())
    number = input()
    counter = 0
    for y in range(total//2):
        if number[y] != number[total-y-1]:
            counter += 1
    if change < counter:
        result += "NO\n"
    else:
        if counter == change:
            result += "YES\n"
        elif total%2 != 0:
            result += "YES\n"
        elif (change-counter)%2 == 0 and total%2 == 0:
            result += "YES\n"
        else:
            result += "NO\n"
print(result[:-1])