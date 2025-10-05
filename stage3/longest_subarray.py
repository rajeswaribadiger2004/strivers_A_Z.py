from typing import List
class Solution:
  def subarray(self,arr:List[int],k:int)->int:
    length=0
    n=len(arr)
    for i in range(n):
      for j in range(i,n):
        s=0
        for x in range(i,j+1):
          s+=a[x]
         if s==k:
                    length=max(length,j-i+1)
        return length
        
if __name__=="__main__":
    sol=Solution()
    arr=[2,3,4,5,6,9,1]
    res=sol.subarray(arr,5)
    print(res)

#o(n3) o(1)
  
