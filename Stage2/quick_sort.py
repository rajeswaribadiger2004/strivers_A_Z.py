# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from typing import List
class Solution:
    def partition(self,arr:List[int],low:int,high:int)->int:
      pivot=arr[low]
      i=low
      j=high
      while i<j:
        while i<high-1 and arr[i]<=pivot:
          i+=1
        while j>low+1 and arr[j]>=pivot:
          j-=1
        if i<j:
          arr[i],arr[j]=arr[j],arr[i]
      arr[j],arr[i]=arr[i],arr[j]
      return j
    
    def quick_sort(self,arr:List[int],low:int,high:int)->int:
      while low<high:
          pIndex=self.partition(arr,low,high)
          self.partition(arr,low,pIndex-1)
          self.partition(arr,pIndex+1,high)
    
    def sortArray(self,nums:List[int])->List[int]:
      self.quick_sort(nums,0,len(nums)-1)
      return nums
    
if __name__=="__main__":
     sol=Solution()
     arr=[2,3,6,4,8,5]
     res=sol.sortArray(arr)



# Time Complexity: O(N*logN), where N = size of the array.
# Worst Case Time complexity: O(n2) 
# Time Complexity for the best and average case: O(N*logN)

# Space Complexity: O(1) + O(N) auxiliary stack space.
     print(res)
