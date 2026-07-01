from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # LinkedList -> List
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        left = 0
        right = len(arr) - 1
        ans = -12345
        while left < right:
            ans = max(ans, arr[left] + arr[right])

            left += 1
            right -= 1

        return ans