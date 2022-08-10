#
from typing import Counter


# words = ["a","b","c","ab","bc","abc"]
# s = "abc"
words = ["a","a"]
s = "aa"
sum_out = 0
i=0
j=0
while(j<len(s)):
    print(s[i:j+1],type(s[i:j+1]))
    sum_out+=words.count(s[i:j+1])
    j+=1
print(sum_out)
# return sum_out