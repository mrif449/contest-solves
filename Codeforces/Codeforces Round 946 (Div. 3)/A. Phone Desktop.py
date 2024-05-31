import math
number = int(input())
for a in range(number):
    x,y = map(int,input().split())
    booked = 0
    remaining = 0 
    if y%2 == 0:
        booked += y/2
        remaining += booked*7
    else:
        booked = math.ceil(y/2)
        remaining += booked*7+4
    if x <= remaining:
        print(int(booked))
    else:
        last = x-remaining
        booked += math.ceil(last/15)
        print(int(booked))