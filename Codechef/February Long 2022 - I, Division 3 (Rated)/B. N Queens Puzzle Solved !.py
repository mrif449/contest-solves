import math
result = ""
case = int(input())
for x in range(case):
    number = int(input())
    answer = (0.143*number)**(number)
    absd = math.floor(answer)
    if answer-absd >= 0.5:
        absd += 1
    result += str(absd)+"\n"
print(result)