# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 노드가 0개거나 1개 있을 경우 바로 return 
        if not head or not head.next:
            return head

        odd_head = head

        # 짝수번째 노드들로만 이루어진 even의 첫 번째 노드를 기억
        even_head = head.next

        odd = odd_head
        even = even_head

        # 홀수번째 노드는 짝수 노드의 다음 노드,
        # 짝수번째 노드는 홀수 노드의 다음 노드를 가르키도록 재배열
        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        # 홀수번째 노드들로 이루어진 링크드 리스트의 마지막이
        # 짝수번째 노드들로 이루어진 링크드 리스트의 첫번째를 가르키도록
        odd.next = even_head

        return head
        

