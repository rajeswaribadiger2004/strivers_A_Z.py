from typing import List
class Solution:
    def maximum(self,arr:List[int])->int:
        maxi=0
        count=0
        for i in range(len(arr)):
            if arr[i]==1:
                count+=1
            else:
                count=0
            maxi=max(maxi,count)
        return maxi           
if __name__=="__main__":
    sol=Solution()
    arr=[1,1,1,1,0,1]
    res=sol.maximum(arr)
    print(res)

    
