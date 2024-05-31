result = ""
number = int(input())
for x in range(number):
    r,c = map(int,input().split())
    period = "+-"*(c)+"+\n"
    regular = "|."*c+"|\n"
    first_line = ".."+"+-"*(c-1)+"+\n"
    second_line = ".."+"|."*(c-1)+"|\n"
    result += "Case #"+str(x+1)+":\n"+first_line+second_line+(period+regular)*(r-1)+period
print(result)