from typing import List
class Solution:
  def Rotate(self,arr:List[int],k:int,direction:str)->List[int]:
    n=len(arr)
    if n==0:
      return arr
    k%=n
    if direction=="right":
      arr[:]=arr[-k:]+arr[:-k]
    elif direction=="left":
      arr[:]=arr[k:]+arr[:k]
    else:
      raise ValueError("Direction must be 'left' or 'right'")
    return arr

if __name__=="__main__":
  sol=Solution()
  res=sol.Rotate( [1,2,3,4,5,6,7],2,"right")
  print(res)
    
#o(n) both tc sc
    
