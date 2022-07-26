s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

# 法1，构建空字符串，再往里面加内容
dic_data = {}
for i in range(len(indices)):
    dic_data[indices[i]] = s[i]
print(dic_data)
str_result = ''
for i in range(len(s)):
    str_result+=dic_data.get(i)
print(str_result)
# return str_result

# 法2,构建空列表，将indices对于索引处添加对应值
result = ['']*len(s)
for i,char in enumerate(s):
    print(i,char)
    result[indices[i]] = char
    # print(result)
print(''.join(result))
# return ''.join(result)