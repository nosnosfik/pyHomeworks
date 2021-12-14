def sum_binary_1(data):
    sum_1 = 0
    for i in f'{data:b}':
        if i != 0:
            sum_1 += int(i)
    if sum_1 == 0:
        sum_1 = None
    return sum_1