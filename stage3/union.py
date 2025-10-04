from typing import List
class Solution:
  def union(self,arr1:list[int],arr2:list[int])->list[int]:
      s=set()
      union=[]
      for num in arr1:
          s.add(num)
      for num in arr2:
          s.add(num)
      union = sorted(list(s))
      return union

  
if __name__=="__main__":
  sol=Solution()
  arr1=[1,2,3,4,5]
  arr2=[2,4,6,7,4]
  res=sol.union(arr1,arr2)
  print(res)

#0((m+n)log(m+n))
#o(m+n)
