number = int(input())
for x in range(number):
    n,m = map(int,input().split())
    if (n%2 == 0 and n>=m and m%2==0) or n%2 == 1 and n>=m and m%2==1:
        print("Yes")
    else: print("No")