def solution():
    a, b = map(int, input().split())
    for i in range(30):
        if (a & (1 << i)) != (b & (1 << i)):
            print(1 << i)
            break


number = int(input())
for _ in range(number):
    solution()