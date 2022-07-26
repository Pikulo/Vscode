from stack import Stack
def parchecker(string_symbol):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string_symbol) and balanced:
        symbol = string_symbol[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False # 判断栈s是否为空
            else:
                s.pop()
        print(s.look(),type(s.look))
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(parchecker('((())'))

