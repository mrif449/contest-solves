number = int(input())
 
for x in range(number):
    a,b = map(int,input().split())
    if a>b:
        print(f"{b} {a}")
    else: print(f"{a} {b}")