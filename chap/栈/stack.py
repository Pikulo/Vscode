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
    # 1. The pop method is defined in the Stack class.
    # 2. The pop method is called on the self object.
    # 3. The pop method returns the last item in the list.
    # 4. The last item in the list is removed from the list.
    # 5. The last item is returned to the calling method.
    def pop(self):
        return self.items.pop()
    # 1. The peek method returns the last item in the list.
    # 2. The peek method does not remove the last item.
    # 3. The peek method can be called from outside the Stack class.
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
