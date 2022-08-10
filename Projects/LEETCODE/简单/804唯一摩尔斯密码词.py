import string


# words = ["gin", "zen", "gig", "msg"]
words = ["a"]
m=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
dict_code={}
# print(list(string.ascii_letters[:26]))
list_letter=list(string.ascii_letters[:26])
for i in range(len(m)):
    dict_code[list_letter[i]]=m[i]
# print(dict_code)
list_coded=[]#存放加密后的内容
for i in words:
    str=''
    for j in i:
        str+=dict_code[j]
    list_coded.append(str)
print(list_coded)
print(len(set(list_coded)))

