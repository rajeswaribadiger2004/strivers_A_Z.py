from typing import List
class Solution:
    def Left(self,arr:List[int])->List[int]:
        n=len(arr)
        if n==0:
            return arr
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
        return arr
        
if __name__=="__main__":
    sol=Solution()
    arr=[1,2,3,4,5]
    res=sol.Left(arr)
    for num in res:
        print(num,end=" ")
