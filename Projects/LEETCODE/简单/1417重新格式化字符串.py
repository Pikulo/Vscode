# s = "a0b1c2u"
# s = "a1"
# s = "leetcode"
# s = "1229857369"
# s = "covid2019"
s = "ab123"

# print(s.sort())
str_num = ''.join([i for i in s if i.isdigit()])
str_cha = ''.join([i for i in s if i.isalpha()])
# print(str_num, str_cha)
a = len(str_num)
b = len(str_cha)
m = ''
order = 0
# print(len(m)) # 0
i = 0
j = 0
if abs(a-b)<=1: #a,b>0表示字母或者数字不为空
    if a>=b:
        first = str_num
        second = str_cha
    else:
        first = str_cha
        second = str_num
    while i < len(first) or j < len(second):
        if not order:
            m+=first[i]
            i+=1
        else:
            m+=second[j]
            j+=1
        order = 1 - order
    print(m)
    # return m
else:
    print('')
    # return ''

