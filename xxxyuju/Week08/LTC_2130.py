from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head

        # linked list의 값을 저장할 배열
        arr = []
        max_sum = 0

        # 값 저장
        while cur:
            arr.append(cur.val)
            cur = cur.next

        n = len(arr)
        for i in range(n//2):
            # i번째 값과 뒤에서 i번째 값을 더해서 최댓값 갱신
            max_sum = max(max_sum, arr[i] + arr[n-i-1])

        return max_sum

