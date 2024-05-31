from math import ceil
test_case = int(input())
for i in range(test_case):
    a_p_hero,i_h_hero,monsterNumber = map(int,input().split())
    monsterPower = list(map(int, input().split())) #length = monesterNumber
    monsterHealth = list(map(int, input().split())) #length = monesterNumber
    count = 0
    damage = 0
    for x in range(monsterNumber):
        count += ceil(monsterHealth[x]/a_p_hero)
        hit = ceil(monsterHealth[x]/a_p_hero)
        damage += hit*monsterPower[x]
    total = i_h_hero-damage
    for j in range(monsterNumber):
        if total+monsterPower[j] > 0:
            print("Yes")
            break
        elif j == monsterNumber-1:
            print("No")