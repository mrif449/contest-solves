def can_sort_array(n, arr):
    if arr == sorted(arr):
        return 'Yes'
 
    sorted_arr = sorted(arr)
    for i in range(n):
        if arr[i:] + arr[:i] == sorted_arr:
            return 'Yes'
    return 'No'
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(can_sort_array(n, arr))