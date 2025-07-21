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

# if __name__ == '__main__':
#     line ='aaabbbccc' #input() + '$'

#     res = []
#     group_start_idx = 0
#     for idx in range(1, len(line)):
#         if line[idx] != line[idx-1]:
#             ln = idx - group_start_idx
#             res.append( (-ln, line[idx-1]) )
#             group_start_idx = idx

#     res.sort()
#     for idx, (freq, char) in enumerate(res):
#         freq = -freq
#         if freq == 1:
#             res[idx] = char
#         else:
#             res[idx] = '{}{}'.format(freq, char)

#     print('_'.join(res))

# def our_replace(main_str, pattern, repalce_with):
#     idx = 0
#     new_str = ''
#     n = len(pattern)

#     while idx < len(main_str):
#         substr = main_str[idx:idx + n]

#         if substr == pattern:
#             new_str += repalce_with
#             idx += n
#         else:
#             new_str += main_str[idx]
#             idx += 1

#     return new_str 


# print(our_replace('aabcabaaad', 'aa', 'x'))

# def containsDuplicate(nums: list[int]) -> bool:
#     freq = [0] * (max(nums) + 1)
    
#     for value in nums:
#         freq[value] += 1
    
#     for i in range(len(freq)):
#         if freq[i] > 1:
#             return True
#     return False

# print(containsDuplicate([1,2,3,2]))


# def isPalindrome(s: str) -> bool:
#         s.replace(',', '').replace(':', '').replace(' ', '').lower()
#         return s == s[::-1]

# print(isPalindrome("A man, a plan, a canal: Panama"))

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))