# 给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。

# 如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。
import re


num = "1210"
num = "030"
res = True
for i in range(len(num)):
    print(num[i],num.count(str(i)))
    if int(num[i]) != int(num.count(str(i))):
        res = False
print(res)
# return res
