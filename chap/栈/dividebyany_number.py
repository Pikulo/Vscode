# my idea
from stack import Stack
def dividebyany_number1(decNumber,base):
    remstack = Stack()
    biggerthan10 = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    while decNumber>0:
        rem = decNumber%base
        if decNumber%base>9:
            remstack.push(biggerthan10.get(rem))
        else:
            remstack.push(rem)
        decNumber = decNumber//base
    binString = ''
    while not remstack.isEmpty():
        binString+=str(remstack.pop())
    return binString
print(dividebyany_number1(233,16))

# other idea
# 构建字符串，对应输出digits[remstack.pop()]来保证一一对应。
def dividebyany_number2(decNumber,base):
    remstack = Stack()
    digits = '0123456789ABCDEF'
    while decNumber>0:
        rem = decNumber%base
        remstack.push(rem)
        decNumber = decNumber//base
    binString = ''
    while not remstack.isEmpty():
        binString+=digits[remstack.pop()]
    return binString
print(dividebyany_number2(233,16))