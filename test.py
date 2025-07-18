


def maxium_sum_fixed_window(lst, k):
    assert k <= len(lst)

    # Compute accumulate sum: A[i] = Sum of all previous elements
    for idx in range(1, len(lst)):
        lst[idx] += lst[idx - 1]

    start_idx, max_sum = 0, lst[k - 1]

    # idx here is actually the last element in the list
    for idx in range(k, len(lst)):
        window = lst[idx] - lst[idx - k]

        if max_sum < window:
            max_sum, start_idx = window, idx - (k - 1)

    return start_idx, max_sum

lst = [1, 0, 3, -4, 2, -6, 9]
maxium_sum_fixed_window(lst, 3)