# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        node = head

        while node:
            next_node = node.next   # 다음 노드 기억
            node.next = prev    # 
            prev = node # 현재 노드를 prev 링크드 리스트 노드
            node = next_node

        return prev







