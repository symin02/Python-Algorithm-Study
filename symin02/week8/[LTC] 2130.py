# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 정확히 절반(후반부 시작점) 찾기
        slow = head
        fast = head

        # 노드가 항상 짝수라서 fast가 끝에 도달할 때까지만 뜀
        while fast:
            fast = fast.next.next # 토끼는 2칸씩
            slow = slow.next        # 거북이는 1칸씩

        # 후반부 리스트의 화살표 방향을 거꾸로 뒤집기
        prev = None
        
        while slow:
            next = slow.next        # 다음 노드 백업
            slow.next = prev        # 화살표 방향을 뒤로 돌림
            prev = slow             # prev를 현재 위치로 한 칸 전진
            slow = next             # slow도 아까 백업해둔 다음 위치로 한 칸 전진
       
       # 양 끝에서 출발하여 최대 짝궁 합 구하기
        maxsum = 0

        while prev and head:
            # 양 끝 값을 더해서 최댓값 갱신
            maxsum = max(maxsum, prev.val + head.val)
            # 안쪽으로 한 칸씩 전진
            prev = prev.next
            head = head.next

        return maxsum