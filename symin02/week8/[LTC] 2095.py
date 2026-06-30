# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 와 진짜 모르겟다

class Solution:
    def deleteMiddle(self, head: optional[ListNode]) -> optional[ListNode]:
        # 노드가 딱 1개면, 어차피 head.next가 None이니까 바로 None을 리턴 (예외 처리)
        if not head.next:
            return head.next
            
        slow = head # 1칸씩 가는 거북이 
        fast = head # 2칸씩 가는 토끼
        temp = head # 거북이의 바로 앞자리를 계속 쫓아다니며 기억할 그림자 포인터
        
        while fast and fast.next:
            #slow가 전진하기 직전에, 그 자리를 temp에게 기억시킴
            temp = slow          
            slow = slow.next       # 거북이 1칸 전진
            fast = fast.next.next  # 토끼 2칸 전진
            
        # 루프가 끝나면 slow는 중간 노드, temp는 중간 노드 바로 앞에 위치
        # temp의 다음 다리를, slow의 다음 다리에 연결해서 slow를 완벽하게 건너뛰게(지우게) 만듭니다.
        temp.next = slow.next
        
        return head