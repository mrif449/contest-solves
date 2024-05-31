result = ""
number = int(input())
for x in range (1,number+1):
        a,b,c,d = map(int,input().split())
        e,f,g,h = map(int,input().split())
        i,j,k,l = map(int,input().split())
        lowest = [min(a,e,i),min(b,f,j),min(c,g,k),min(d,h,l)]
        final = [0,0,0,0]
        report = sum(lowest)
        target = 1000000
        if report >= target:
            if lowest[0] >= target:
                final[0] = 1000000
                final[1] = 0
                final[2] = 0
                final[3] = 0
            elif lowest[1] >= target:
                final[0] = 0
                final[1] = 1000000
                final[2] = 0
                final[3] = 0
            elif lowest[2] >= target:
                final[0] = 0
                final[1] = 0
                final[2] = 1000000
                final[3] = 0
            elif lowest[3] >= target:
                final[0] = 0
                final[1] = 0
                final[2] = 0
                final[3] = 1000000
            else:
                final[0] = lowest[0]
                if lowest[0] + lowest[1] >= 1000000:
                    final[1] = 1000000-final[0]
                    result += f"Case #{str(x)}: {str(final[0])} {str(final[1])} {str(final[2])} {str(final[3])}\n"
                    continue
                else:
                    final[1] = lowest[1]
                if lowest[0] + lowest[1] + lowest[2] >= 1000000:
                    final[2] = 1000000- (lowest[0] + lowest[1])
                    result += f"Case #{str(x)}: {str(final[0])} {str(final[1])} {str(final[2])} {str(final[3])}\n"
                    continue
                else:
                    final[2] = lowest[2]
                if lowest[0] + lowest[1] + lowest[2] + lowest[3] >= 1000000:
                    final[3] = 1000000 - (lowest[0] + lowest[1] + lowest[2])
                    result += f"Case #{str(x)}: {str(final[0])} {str(final[1])} {str(final[2])} {str(final[3])}\n"
                    continue
                else:
                    final[3] = lowest[3]
            result += f"Case #{str(x)}: {str(final[0])} {str(final[1])} {str(final[2])} {str(final[3])}\n"      
        else:
            result += f"Case #{str(x)}: IMPOSSIBLE\n"
print(result[:-1])