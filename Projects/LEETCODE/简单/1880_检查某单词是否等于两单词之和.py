# 字母的 字母值 取决于字母在字母表中的位置，从 0 开始 计数。即，'a' -> 0、'b' -> 1、'c' -> 2，
# 以此类推。 对某个由小写字母组成的字符串 s 而言，其 数值 就等于将 s 中每个字母的 字母值 
# 按顺序 连接 并 转换 成对应整数。 例如，s = "acb" ，依次连接每个字母的字母值可以得到 "021" ，
# 转换为整数得到 21 。 给你三个字符串 firstWord、secondWord 和 targetWord ，每个字符串都由
# 从 'a' 到 'j' （含 'a' 和 'j' ）的小写英文字母组成。 如果 firstWord 和 secondWord 的 数值
# 之和 等于 targetWord 的数值，返回 true ；否则，返回 false 。


firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
'''my idea'''
dict_alph = {}
index = 'a'
for i in range(0,26):
    dict_alph[index] = i
    index = chr(ord(index)+1)
print(dict_alph)
res = []
sum = 0
for i in firstWord:
    res.append(str(dict_alph[i]))
# print(res)
sum+=int(''.join(res))
res = []
for i in secondWord:
    res.append(str(dict_alph[i]))
sum+=int(''.join(res))
print(sum)
res = []
for i in targetWord:
    res.append(str(dict_alph[i]))
print(sum==int(''.join(res)))
# return sum==int(''.join(res))

# prefer idea
dict_alph = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7', 'i': '8', 'j': '9'}
print(int(''.join(dict_alph[i] for i in firstWord))+\
      int(''.join(dict_alph[i] for i in secondWord))==\
      int(''.join(dict_alph[i] for i in targetWord)))
# return int(''.join(dict_alph[i] for i in firstWord))+\
#       int(''.join(dict_alph[i] for i in secondWord))==\
#       int(''.join(dict_alph[i] for i in targetWord))
