result = ""
case = int(input())
for x in range(case):
    length = int(input())
    store = []
    data = input()
    sum = 0
    for y in data:
        if y not in store:
            store.append(y)
            sum += 2
        else:
            sum += 1
    result += str(sum)+"\n"
print(result[:-1])
