from stack import Stack
def divideby2(decNumber):
    remstack = Stack()
    while decNumber>0:
        rem = decNumber%2
        remstack.push(rem)
        decNumber = decNumber//2
    binString = ''
    while not remstack.isEmpty():
        binString+=str(remstack.pop())
    return binString
print(divideby2(1000))
# 通过修取余数，可切换成10进制和8进制。
