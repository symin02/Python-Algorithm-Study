from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 노드가 없거나 하나뿐이면 그대로 반환
        if not head or not head.next:
            return head

        odd = head
        even = head.next


        # 짝수 리스트의 head 저장
        even_first = even

        while even and even.next:
            # 현재 odd 뒤 다음 홀수번째 노드 연결
            odd.next = even.next
            odd = odd.next

            # 현재 even 뒤 다음 짝수번째 노드 연결
            even.next = odd.next
            even = even.next

        # 홀수와 짝수 리스트 연결
        odd.next = even_first

        return head