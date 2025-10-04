from typing import List
class Solution:
  def linear_search(self,arr:List[int],num:int)->int:
    for i in range(len(arr)):
      if arr[i]==num:
        return i
    return -1

if __name__=="__main__":
  sol=Solution()
  arr=[2,3,4,5]
  num=5
  res=sol.linear_search(arr,num)
  print(res)

#o(n) o(1)
