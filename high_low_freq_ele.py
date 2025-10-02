# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
 # return highest freq element, lowest freq element
from typing import List,Tuple
class Solution:
  def freq(self,arr:List[int])->Tuple[int,int]:
    mp={}
    for num in arr:
      mp[num]=mp.get(num,0)+1

    maxEle=minEle=None
    maxFreq=0
    minFreq=len(arr)

    for element,count in mp.items():
      if count>maxFreq:
        maxFreq=count
        maxEle=element

      if count<minFreq:
        minFreq=count
        minEle=element

    return (maxEle,minEle)
if __name__ == "__main__":
    arr = [10, 5, 10, 15, 10, 5]
    sol = Solution()
    maxEle, minEle = sol.freq(arr)
    print("The highest frequency element is:", maxEle)
    print("The lowest frequency element is:", minEle)  
            
            
      
