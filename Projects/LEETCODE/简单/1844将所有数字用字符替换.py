s = "a1c1e1"
s = "a1b2c3d4e"

# my idea
res = ''
print(res+'4')
for i in range(len(s)):
    if s[i].isdigit():
        res+=chr(ord(s[i-1])+int(s[i]))
    else:
        res+=s[i]
print(res)
# return res

# other idea
s = list(s)
for i in range(1,len(s),2):
    s[i]=chr(ord(s[i-1])+int(s[i]))
print(''.join(s))
# return ''.join(s)