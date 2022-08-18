"""节点类"""
class LinkedNode:
    '''实例化单链表的类时：定义两个成员变量：一个是head指针，一个是节点存储的值'''

    def __init__(self, val, prev=None, next=None):
        self.val = val # 链表值
        self.prev = prev # 链表头节点
        self.next = next # 链表尾节点


class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.len = 0
        self.head = LinkedNode(-1)
        self.head.next = self.head.prev = self.head
a = MyCircularDeque(3)
print(a.k)
