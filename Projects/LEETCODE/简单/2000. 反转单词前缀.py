from __future__ import barry_as_FLUFL


word = "abcdefd"
ch = "d"
word = "xyxzxe"
ch = "z"
word = "abcd"
ch = "z"
index = 0
for i in range(len(word)):
    if word[i]==ch:
        index = i
        break
print(index,word[index::-1],word[index+1:])
word = word[index::-1]+word[index+1:]
print(word)
# return word