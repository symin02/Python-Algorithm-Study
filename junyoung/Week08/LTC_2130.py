# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        arr = []
        node = head

        # node 값들을 배열에 저장
        while node:
            arr.append(node.val)
            node = node.next
        
        length = len(arr)
        m = 0
        # 한 쌍의 합들 중 가장 큰 값을 구함
        for i in range(len(arr) // 2):
            m = max(m, arr[i] + arr[length - 1 - i])

        return m