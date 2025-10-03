from typing import List
class Solution:
  def largest(self,arr:List[int])->int:
    largest=arr[0]
    for i in range(len(arr)):
      if arr[i]>largest:
        largest=arr[i]
    return largest
                
if __name__=="__main__":
    sol=Solution()
    arr=[2,5,3,7,8]
    res=sol.largest(arr)
    print(res)

#recursive approach
