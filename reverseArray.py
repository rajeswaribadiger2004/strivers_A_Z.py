from typing import List
class Solution:
  def reverseArray(self,arr:List[int])->List[int]:
    p1=0
    p2=len(arr)-1
    while p1<p2:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
        p2-=1
    return arr
   
if __name__ == "__main__":
    sol = Solution()
    arr = [5, 4, 3, 2, 1]
    reversed_arr = sol.reverseArray(arr)
    
    print("The reversed array is:-")
    print(*reversed_arr)
