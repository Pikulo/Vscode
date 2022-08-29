from string import ascii_lowercase, ascii_uppercase
import string


key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
dict_code = {' ':' '}
a = 'a'
for i in key:
    if i.isalpha() and i not in dict_code:
        print(i)
        dict_code[i]=a
        a=chr(ord(a)+1)
print(dict_code)
print(''.join(dict_code[i] for i in message))
# return ''.join(dict_code[i] for i in message)

print(ascii_lowercase)
print(ascii_uppercase)
print(string.ascii_letters)