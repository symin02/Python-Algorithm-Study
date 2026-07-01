# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None    # 이전 노드를 기억할 포인터 
        curr = head    # 현재 내가 서 있는 노드 
        
        while curr:
            #다리를 뒤집기 전에, 원래 가야 할 다음 노드를 미리 백업
            next_temp = curr.next 
            
            #현재 노드의 화살표 방향을 이전 노드 쪽으로 보냄
            curr.next = prev
            
            #다음 턴을 위해 포인터들을 나란히 한 칸씩 앞으로 전진
            prev = curr
            curr = next_temp
            
        # 루프가 끝나면 curr는 None으로 떨어지고, prev가 가장 마지막 노드에 위치
        return prev