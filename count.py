class Solution:
    def countDigits(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += 1
            n //= 10
        return cnt

# s = Solution()
# print(s.countDigits(329823))  # Output: 6
# print(s.countDigits(7))       # Output: 1
# print(s.countDigits(10000))   # Output: 5

..................optimal................
import math

def countDigits(n):
    if n == 0:
        return 1
    return int(math.log10(n) + 1)
