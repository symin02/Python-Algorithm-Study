from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getLen(self, head):
        cnt = 0
        cur = head
        li = []
        while cur:
            li.append(cur.val)
            cnt += 1
            cur = cur.next
        return cnt, li

    def toLinkedList(self, li):
        new_li = ListNode(0)
        cur = new_li
        for num in li:
            cur.next = ListNode(num)
            cur = cur.next

        # new_li는 ListNode(0)을 바라보고 있기 때문에
        # head를 리턴하기 위해서 new_li.next 해야함
        return new_li.next

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, li = self.getLen(head)
        del li[n // 2]
        return self.toLinkedList(li)