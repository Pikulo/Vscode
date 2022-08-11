# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head
        for _ in range(k):
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter

a = [1, 2, 3, 4, 5]
for i in a:
    print(ListNode(i).next)
# print(Solution.getKthFromEnd(a, 2))
