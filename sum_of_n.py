class Solution:
  def func(self,n:int)->None:
    sum=0
    for i in range(1,n+1):
      sum+=n
    print(sum)

if __name__=="__main__":
  sol=Solution()
  sol.func(7)
  
