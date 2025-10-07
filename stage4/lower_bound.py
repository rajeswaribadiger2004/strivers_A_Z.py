from typing import List

class Solution:
    def lowerBound(self, arr: List[int], n: int, x: int) -> int:
        low = 0
        high = n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] >= x:
                ans = mid
                # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right

        return ans
#o(logn) o(1)
