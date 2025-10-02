from typing import List
class Solution:
    def bubble(self,arr:List[int])->List[int]:
        n=len(arr)
        for i in range(n):
            swapped=False
            for j in range(0,n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swapped = True
            if not swapped:   
                break
        return arr
if __name__=="__main__":
    arr=[2,4,8,3,5]
    sol=Solution()
    sorted=sol.bubble(arr)
    print(sorted)

#o(n2) but optimized o(n)
