from typing import List
class Solution:
    def sorted(self,arr:List[int])->bool:
        n=len(arr)
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                return True
        return False
        
if __name__=="__main__":
    sol=Solution()
    arr=[2,3,4,5]
    res=sol.sorted(arr)
    print(res)
