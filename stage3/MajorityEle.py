from collections import Counter
class Solution:
  def Majority(self,arr:List[int])->int:
    n=len(arr)
    count=Counter(arr)
    for num,freq in items.count():
      if freq>n//2:
        return num

    return -1
    #o(nlogn)+o(n)
