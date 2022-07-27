# Time Complexity: O(n)
class Queue:
    """实现一个队列"""
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        """入队"""
        # Time Complexity: O(n)
        return self.items.insert(0,item)
    
    # It creates a function called look that takes self as a parameter.
    def look(self):
        return self.items

    def dequeue(self):
        """出队"""
        # Time Complexity: O(1)
        return self.items.pop()

    def isEmpty(self):
        return not self.items

    def size(self):
        """队列的大小"""
        return len(self.items)

# Time Complexity: O(1)
# Creates a queue object.
# The Queue class is a FIFO (first in, first out) data structure that can store any Python object.
# 
# Args:
#   self: the name of the object.
# Returns:
#   The return value is the number of items that were removed from the queue.


# my_queue = Queue()
# my_queue.enqueue(1)
# my_queue.enqueue(2)
# my_queue.enqueue(3)
# my_queue.enqueue(4)
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.dequeue())
# print(my_queue.isEmpty())
# print(my_queue.size())