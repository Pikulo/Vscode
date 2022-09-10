# 给你一个字符串 s 和一个字符 letter ，返回在 s 中等于 letter 字符所占的 百分比 ，向下取整到最接近的百分比。

import math


s = "foobar"
letter = "o"
cou = 0
for i in s:
    if i==letter:
        cou+=1
print(math.floor(cou/len(s)*100))
print(cou*100//len(s))
# return math.floor(cou/len(s)*100)