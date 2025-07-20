# def filtering(str):
#     last_idx, res = 0, []
#     for idx, char in enumerate(str):
#         if char in ',#$':
#             val = str[last_idx : idx]
#             if val.strip():
#                 res.append(val)
#             last_idx = idx + 1
#     return res


# string = 'apple,banana, , , apple,student### #student$$apple'

# print(filtering(string))


# def compressing(string):
#     res = ''
#     for idx in range(1, len(string)):
#         if string[idx] != string[idx -1]:
#             res += str(string.count(string[idx - 1])) + string[idx - 1] + '_'
#     res += str(string.count(string[idx])) + string[-1]
#     return res

# string = 'z'
# print(compressing(string))

if __name__ == '__main__':
    line ='aaabbbccc' #input() + '$'

    res = []
    group_start_idx = 0
    for idx in range(1, len(line)):
        if line[idx] != line[idx-1]:
            ln = idx - group_start_idx
            res.append( (-ln, line[idx-1]) )
            group_start_idx = idx

    res.sort()
    for idx, (freq, char) in enumerate(res):
        freq = -freq
        if freq == 1:
            res[idx] = char
        else:
            res[idx] = '{}{}'.format(freq, char)

    print('_'.join(res))