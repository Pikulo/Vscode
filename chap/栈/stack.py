#python实现栈的定义
class Stack:
    # 定义一个列表/构造一个栈
    def __init__(self):
        self.items = []
        # print("你创造了一个栈！")
    def isEmpty(self):
        return self.items == []
    def look(self):
        # print(self.items)
        return self.items
    def push(self, item):
        self.items.append(item)
        # print("你给栈顶加了个%s" % item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
