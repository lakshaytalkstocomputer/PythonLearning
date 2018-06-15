def unique_list(l):
    n = list()
    for ele in l:
        if ele not in n:
            n.append(ele)
    return n
