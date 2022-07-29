# 1. The class Deque() creates a new instance of the Deque class.
# 2. The __init__() method is a special method that is called when an instance of the class is created.
# 3. The __init__() method creates an empty list to store the items in the Deque.
# 4. The isEmpty() method checks to see if the Deque is empty.
# 5. The addFront() method adds a new item to the “front” or “head” of the Deque.
# 6. The addRear() method adds a new item to the “rear” or “tail” of the Deque.
# 7. The removeFront() method removes an item from the “front” or “head” of the Deque.
# 8. The removeRear() method removes an item from the “rear” or “tail” of the Deque.
# 9. The size() method returns the number of items in the Deque.
class Deque():
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    # Time Complexity: O(1)
    def addFront(self,item):
        self.items.append(item)
    
    # Time Complexity: O(n)
    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def look(self):
        return self.items

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.addFront(1)
d.addFront(2)
d.addRear('zero')
print(d.look())