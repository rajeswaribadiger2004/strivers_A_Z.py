from typing import List,Dict
class Solution:
  def freq(self,arr:List[int])->Dict[int,int]:
    mp={}
    for num in arr:
      mp[num]=mp.get(num,0)+1
    return mp

if __name__=="__main__":
  arr = [10, 5, 10, 15, 10, 5]
  sol = Solution()
  ans = sol.freq(arr)
  print(ans)

#O(n + k)  ≈  O(n)

    
