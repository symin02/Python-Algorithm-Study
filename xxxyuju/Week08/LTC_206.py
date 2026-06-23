from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        reverse_head = None
        cur = head

        while cur:
            # cur.next를 바꾸기 전에 다음 노드 저장
            next_node = cur.next

            # 현재 노드가 reverse된 리스트의 맨 앞을 가리키도록
            cur.next = reverse_head

            # 현재 노드가 reverse된 리스트의 맨 앞
            reverse_head = cur

            # 다음 노드로 이동
            cur = next_node

        return reverse_head