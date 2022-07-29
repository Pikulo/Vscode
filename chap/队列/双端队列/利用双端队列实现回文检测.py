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
        print(first_char,last_char)
        if first_char!=last_char:
            stillequal = False
    return stillequal

print(palchecker('toot'))