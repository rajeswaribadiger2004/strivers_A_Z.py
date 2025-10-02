from typing import List
class Solution:
  def insertion(self,arr:List[int])->List[int]:
    n=len(arr)
    for i in range(1,n):
      j=i
      while j>0 and arr[j-1]>arr[j]:
        arr[j],arr[j-1]=arr[j-1],arr[j]
        j-=1
    return arr
           
if __name__=="__main__":
    arr=[2,4,8,3,5]
    sol=Solution()
    sorted=sol.insertion(arr)
    print(sorted)

#o(n2) o(1)
