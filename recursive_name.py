class Solution:
  def func(self,i:int,n:int)->None:
    if i>n:
      return
    print("Raj")
    self.func(i+1,n)
if __name__=="__main__":
    sol=Solution()
    n=4
    sol.func(1,n)
