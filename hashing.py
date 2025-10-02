from typing import List
class Solution:
    def countOccurrences(self, nums: List[int], queries: List[int]) -> List[int]:
        # Step 1: Precompute frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Answer queries in O(1)
        result = []
        for q in queries:
            result.append(freq.get(q, 0))
        return result
if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2]
    queries = [1, 3, 4, 2, 10]

    sol = Solution()
    ans = sol.countOccurrences(nums, queries)
    print(ans) 
  
#Total complexity = O(N + Q)
