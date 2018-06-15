def bool_check(num,low,high):
    l = list(range(low,high+1))
    if num in l:
        return True
    else:
        return False


def bool_check1(num,low,high):
    return num in range(low, high+1)
