from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd, even = head, head.next
        even_start = head.next

        # while문 조건이 어떻게 되어야하는지 모르겟음
        while even and even.next:
            # 노드 연결 바꾸기 + 포인터 옮기기
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_start
        return head