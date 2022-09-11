# 给你一个字符串数组 patterns 和一个字符串 word ，统计 patterns 中有多少个字符串是 word 的子字符串。返回字符串数目。

# 子字符串 是字符串中的一个连续字符序列。

patterns = ["a","abc","bc","d"]
word = "abc"
patterns = ["a","b","c"]
word = "aaaaabbbbb"
res = 0
for i in patterns:
    if i in word:
        res+=1
print(res)
# return res