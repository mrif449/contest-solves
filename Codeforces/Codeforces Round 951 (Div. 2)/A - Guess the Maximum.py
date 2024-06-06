def solution():
    n = int(input())
    a = list(map(int, input().split()))
    mini = max(a[0], a[1])
    for i in range(1, n - 1):
        mini = min(mini, max(a[i], a[i + 1]))
    print(mini - 1)


number = int(input())
for _ in range(number):
    solution()