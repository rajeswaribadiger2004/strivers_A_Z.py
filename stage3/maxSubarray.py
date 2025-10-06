#o(n2) o(1)
from typing import List
import sys
class Solution:
  def Majority(self,arr:List[int])->int:
      maxi=-sys.maxsize-1
      for i in range(n):
          sum=0
          for j in range(i,n):
              sum+=arr[j]
              maxi=max(maxi,sum)
      return maxi
