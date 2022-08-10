word1 = ["ab", "c"]
word2 = ["a", "bc"]
def combine(list_target):
    str_num = ''
    for i in list_target:
        str_num+=i
    return str_num
print(combine(word1),combine(word2))
if combine(word1)==combine(word2):
    # return True
    print(True)
else:
    # return False
    print(False)

#力扣解法
print(''.join(word1)==''.join(word2))