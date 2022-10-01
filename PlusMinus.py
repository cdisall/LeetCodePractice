def plusMinus(arr):
    num_pos = 0
    num_neg = 0
    num_zero = 0
    count = 0
    for x in arr:
        count+=1
        if x>0:
            num_pos+=1
        elif x<0:
            num_neg+=1
        else:
            num_zero+=1
    print(float("{0:.4f}". format(num_pos/count)))
    print(num_neg/count)
    print(num_zero/count)
