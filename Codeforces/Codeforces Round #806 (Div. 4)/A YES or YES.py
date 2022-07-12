result = ""
number = int(input())
for x in range(number):
    data = input()
    if data.lower() == "yes":
        result += "YES\n"
    else:
        result += "NO\n"
print(result[:-1])
