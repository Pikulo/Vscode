# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写
# 英文字符： 字符（'a' - 'i'）分别用（'1' - '9'）表示。 字符（'j' - 'z'）分别用
# （'10#' - '26#'）表示。 返回映射之后形成的新字符串。 题目数据保证映射始终唯一。

from re import A

s = "10#11#12"
s = "1326#"
dic_1 = {}
dic_2 = {}
index_1 = 'a'
index_2 = 'j'
for i in range(1,10):
    dic_1[i] = index_1
    index_1 = chr(ord(index_1)+1)
# print(dic_1)
for i in range(10,27):
    index = str(i)+'#'
    dic_2[index] = index_2
    index_2 = chr(ord(index_2)+1)
# print(dic_2)
res = []
i = len(s)-1
while i>=0:
    if s[i] != '#':
        res.append(dic_1[int(s[i])])
        i-=1
    else:
        res.append(dic_2[s[i-2:i+1]])
        i-=3
# print(res)
print(''.join(res[::-1]))
# return ''.join(res[::-1])
