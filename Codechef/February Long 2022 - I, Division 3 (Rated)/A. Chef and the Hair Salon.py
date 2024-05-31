result = ""
case = int(input())
for x in range(case):
    customer,time = map(int,input().split())
    late = customer*time
    result += str(late)+"\n"
print(result[:-1])