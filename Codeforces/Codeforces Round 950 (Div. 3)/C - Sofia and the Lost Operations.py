def build(arr, brr):
    buf = []
    for i in range(len(arr)):
        if arr[i] != brr[i]:
            buf.append(brr[i])
    buf.sort()
    return buf

def check(brr, drr):
    return any(x == drr[-1] for x in brr)

def solve(arr, brr, drr):
    if not check(brr, drr):
        return False
    drr.sort()
    ib, id = 0, 0
    while ib < len(buf) and id < len(drr):
        if buf[ib] == drr[id]:
            ib += 1
            id += 1
        elif buf[ib] < drr[id]:
            return False
        else:
            id += 1
    return ib == len(buf)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    m = int(input())
    drr = list(map(int, input().split()))
    buf = build(arr, brr)
    if solve(arr, brr, drr):
        print("YES")
    else:
        print("NO")
