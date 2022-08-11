import re
s = "   -42"
# s = "42"
# s = "004193 with296- words"
# s = "    "

# s = s.lstrip()
print(s)
# num_re = re.compile(r'^[\+\-]?\d+')
num = re.findall(r'^[\+\-]?\d+', s.lstrip())
# print(num, *num, type(*num))  # ['-42'] -42 <class 'str'>
print(max(min(int(*num), (1 << 31)-1), -(1 << 31)))
