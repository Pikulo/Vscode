
from stack import Stack
def parchecker(string_symbol):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string_symbol) and balanced:
        symbol = string_symbol[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False # 判断栈s是否为空
            else:
                top = s.pop()
                if not matches(top,symbol): # 增加字符类型匹配
                    balanced = False
        # print(s.look(),type(s.look))
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)
print(parchecker('((()))')) # True
print(matches('(',']')) # False
print(parchecker('{[({[()]})]}')) # True
print(parchecker('[([{}]})]')) # False

# opens = '([{'
# closers = ')]}'
# print(opens.index('('),closers.index(')'))

