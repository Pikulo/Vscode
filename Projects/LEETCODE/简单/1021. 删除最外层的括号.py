# 有效括号字符串为空 ""、"(" + A + ")" 或 A + B ，其中 A 和 B 都是有效的括号字符串，+ 代表字符串的连接。

#     例如，""，"()"，"(())()" 和 "(()(()))" 都是有效的括号字符串。

# 如果有效字符串 s 非空，且不存在将其拆分为 s = A + B 的方法，我们称其为原语（primitive），其中 A 和 B 都是非空有效括号字符串。

# 给出一个非空有效字符串 s，考虑将其进行原语化分解，使得：s = P_1 + P_2 + ... + P_k，其中 P_i 是有效括号字符串原语。

# 对 s 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 s 。

# s = "(()())(())"
# s = "(()())(())(()(()))"
s = "()()"
res= ''
n = len(s)
i = 0
index_left = 0
while i < n:
    if s[i] == '(' and index_left==0:
        index_first=i
    if s[i] == '(':
        index_left+=1
    if s[i] == ')':
        index_left-=1
    if index_left==0:
        index_last=i
        temp = s[index_first:index_last+1]
        if len(temp)!=2:
            res += temp[1:len(temp)-1]
            print(res)
        else:
            res +=''
    i+=1
print(res)

