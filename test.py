
def longest_sublist(lst):
    best_len = None
    
    for start in range(1):
        zeros, ones = 0, 0
        for end in range(start, len(lst)):
            if lst[end] == 0:
                zeros += 1
            else:
                ones += 1
            
            if zeros == ones:
                cur_len = end - start + 1
                if best_len is None or best_len < cur_len:
                    best_len = cur_len
    return best_len

assert longest_sublist([1, 1, 0, 0]) == 4
assert longest_sublist([1, 1, 0, 0, 0, 1]) == 6
