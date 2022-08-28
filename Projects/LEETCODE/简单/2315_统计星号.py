# s = "l|*e*et|c**o|*de|"
# s = "iamprogrammer"
s = "yo|uar|e**|b|e***au|tifu|l"
# s = "|**|*|*|**||***||"

#other idea
# It counts the number of asterisks in the string s.
print(sum(t.count('*') for t in s.split('|')[::2]))


'''
# my  idea
list_tem = []
list_tem2 = []
for i,j in enumerate(s):
    if j == '|':
        list_tem.append(i)
# print(list_tem)
if len(list_tem)>0:
    i =0
    while i <= len(list_tem)-2:
        # print(i)
        # print(s[list_tem[i]:list_tem[i+1]+1])
        list_tem2.append(s[list_tem[i]:list_tem[i+1]+1])
        i +=2
    print(list_tem2)
    for i in list_tem2:
        s = s.replace(i, '',1)
        print(s)
res = 0
for i in s:
    if i == '*':
        res+=1
print(res)
# return res
'''
