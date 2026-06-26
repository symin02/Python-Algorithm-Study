from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 노드가 하나뿐이면 None 반환
        if head.next is None:
            return None

        cnt = 0
        cur = head

        # 노드 개수 세기
        while cur:
            cnt += 1
            cur = cur.next

        # 가운데 노드의 index
        mid = cnt // 2

        idx = -1
        cur = head

        # print(mid)

        # 가운데 직전 노드까지 이동
        while cur:
            idx += 1
            if idx == mid - 1:
                # 가운데 노드를 건너뛰도록 변경
                cur.next = cur.next.next
                break
            cur = cur.next
        
        return head