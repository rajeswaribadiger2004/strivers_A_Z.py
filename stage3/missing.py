from typing import List
class Solution:
    def missing(self,arr:List[int],n:int)->int:
        total_sum=(n*(n+1))//2
        arr_sum=sum(arr)
        return total_sum-arr_sum
        
if __name__ == "__main__":
    n = 5
    arr = [1, 2, 4, 5]
    sol = Solution()
    ans = sol.missing(arr, n)
    print("The missing number is:", ans)
