def foo(data):
    final_list = []
    for i in data:
        list_prod = 1
        for j in data:
            if i == j:
                continue
            else:
                list_prod *= j
        final_list.append(list_prod)
    return final_list