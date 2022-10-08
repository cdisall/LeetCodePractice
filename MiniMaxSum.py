def miniMaxSum(arr):
    s = sum(arr)
    l = [s]*(len(arr))
    for i in range((len(arr))):
        l[i] = l[i]-arr[i]
    print(min(l), max(l))
