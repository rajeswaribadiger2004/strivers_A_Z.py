from typing import List
class Solution:
  def selection(self,arr:List[int])->List[int]:
    n=len(arr)
    for i in range(n-1):
      min=i
      for j in range(i+1,n):
        if arr[j]<arr[min]:
          min=j
      arr[i], arr[min] = arr[min], arr[i]
    return arr
if __name__=="__main__":
    arr=[2,4,8,3,5]
    sol=Solution()
    sorted=sol.selection(arr)
    print(sorted)

#o(n2) o(1)
        
