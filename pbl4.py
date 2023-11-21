def operations_performed(n, arr):
    # for the very first time, checking
    for num in arr:
        if num % 2 != 0: # odd detected
            return 0  # so, no operations performed

    count = 0
    while True:
        flag = 0
        for i in range(0, n, 1):
            if arr[i] % 2 != 0:
                flag = 1
                break
            arr[i] //= 2
            
        if flag is 0: 
            count += 1 #counting how many operations occured
        else:
            break

    return count

n = int(input())
arr = list(map(int, input().split()))

count = operations_performed(n, arr)
print(count)


