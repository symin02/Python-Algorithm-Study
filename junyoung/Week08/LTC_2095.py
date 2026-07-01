# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_head = ListNode(0)
        first_head.next = head

        # 중앙값 가르키는 포인터
        slow = first_head
        fast = head

        # head linked list를 두 칸씩 탐색할 때 slow 포인터는 한 칸만 탐색
        # -> fast의 중간 포인터 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 참조 변경(노드 건너뛰기)
        slow.next = slow.next.next

        return first_head.next


