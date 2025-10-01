class Solution:
  def func(self,i:int,n:int)->None:
    if i>n:
      return
    print(i)
    
    self.func(i+1,n)
if __name__=="__main__":
    sol=Solution()
    n=4
    sol.func(1,n)

  
# prg for N-1
 class Solution:
  def func(self,i:int,n:int)->None:
    if i,1:
      return
    print(i)
    
    self.func(i-1,n)
if __name__=="__main__":
    sol=Solution()
    n=4
    sol.func(n,n)
