

def josephus(n, k):
    lst = [idx + 1 for idx in range(n)] # assign 1 2 3 4 5 ... n

    # Note creating length at once is MORE efficient than N appends

    last_pos = 0
    ret = [0] * n   # let's avoid a lot of appends (if efficiency matters)

    for pos in range(n-1):  # the range will be created once with the original n
        #for step in range(k-1):
        #    last_pos = (last_pos + 1) % n   # % can join these lines!
        last_pos = (last_pos + k - 1) % n

        ret[pos] = lst[last_pos]
        lst.pop(last_pos)
        n = len(lst)  # list is shrinking
        last_pos %= n

    ret[-1] = lst[0]

    return ret

josephus(7, 3)