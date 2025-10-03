from typing import List

class Solution:
    def second_largest(self,arr:List[int])->int:
        n=len(arr)
        if n<2:
            return -1
        largest=float('-inf')
        second_lar=float('-inf')
        for num in range(n):
            if num>largest:
                second_lar=largest
                largest=num
            elif num>second_lar and num!=largest:
                second_lar=num
        return second_lar if second_lar != float('-inf') else -1
        
if __name__ == "__main__":
    sol = Solution()
    arr = [2, 5, 1, 3, 0]
    print("Second largest in arr1:", sol.second_largest(arr)) 

#o(n) o(1)
