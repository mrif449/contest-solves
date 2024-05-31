def max_score(l, r):
    power_of_two = 1
    while power_of_two * 2 <= r:
        power_of_two *= 2

    score = 0
    while power_of_two != 1:
        power_of_two //= 2
        score += 1
    
    return score

t = int(input().strip())

for _ in range(t):
    l, r = map(int, input().strip().split())
    print(max_score(l, r))