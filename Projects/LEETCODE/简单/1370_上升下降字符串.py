import collections


# 1. First, we sort the string in the descending order of their ASCII value.
# 2. Then we create a new string called res.
# 3. We iterate over the sorted string and append the first character to res.
# 4. We then decrement the count of that character in the counter.
# 5. If the character’s count becomes 0, we remove it from the counter.
# 6. We then reverse the flag.
# 7. We again iterate over the sorted string and append the first character to res.
# 8. We then decrement the count of that character in the counter.
# 9. If the character’s count becomes 0, we remove it from the counter.
# 10. We repeat this process until the counter is empty.
# 11. Finally, we join the characters of the res string and print it.
s = "aaaabbbbcccc"
s = "leetcode"
flag = False
res = []
s_counter = collections.Counter(s)
print(s_counter)
while s_counter:
    keys = s_counter.keys()
    keys = sorted(keys,reverse=flag)
    print(keys) 
    flag = not flag
    res.append(''.join(keys))
    print(res)
    s_counter-=collections.Counter(keys)
print(''.join(res))
# return ''.join(res)