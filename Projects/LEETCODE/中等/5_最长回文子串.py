from itertools import combinations
import re
from xml.etree.ElementTree import QName
from deque import Deque


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillequal = True

    while chardeque.size() > 1 and stillequal:
        first_char = chardeque.removeFront()
        last_char = chardeque.removeRear()
        # print(first_char,last_char)
        if first_char!=last_char:
            stillequal = False
    return stillequal

# print(palchecker('tt'))

# s = "babad"
s = "cbbd"
# s = "abcd"
s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
res = []
if len(s)==1:
    print(s)
    # return s
else:
    i=0
    while i<len(s):
        k=i
        while k <len(s):
            if palchecker(s[i:k+1]):
                res.append(s[i:k+1])
            k+=1
        i+=1
res.sort(key=lambda x:len(x),reverse=True)
print(res[0])
# return res[0]
'''当字符串太长了会超出时间限制'''
