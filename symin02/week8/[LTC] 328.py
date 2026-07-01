# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #예외 처리 노드가 아예 없거나 1~2개뿐이면 홀짝을 나눌 필요가 없어서 그대로 반환
        if head is None or head.next is None:
            return head
        
        odds = head                 # 홀수 그룹은 1번째 노드부터 시작
        evens = head.next           # 짝수 그룹은 2번째부터 시작
       
        # 나중에 이어붙여야 하니 백업
        even_head = evens
        # 짝수가 앞서나가니 evens와 evens.next가 존재하는지 확인하며 루프 돌ㄹ기
        while evens and evens.next:
            # 홀 짝 각각 두칸씩 뛰어넘은 칸으로 연결
            odds.next = odds.next.next
            evens.next = evens.next.next

            # 새로 연결한 걸 이용해 포인터들도 다음 자리 이동
            odds = odds.next
            evens = evens.next
        # 루프 다돌면 odds는 홀수 맨 뒷 노드에 위치함, 그 뒤에 짝수 머리 이어줌
        odds.next = even_head

        return head