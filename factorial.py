#resursive( o(N) )
class Solution:
  def fact(self,n:int)->int:
    if n<1:
        return 1
    else:
        return n*self.fact(n-1)
      
if __name__=="__main__":
  sol=Solution()
  res=sol.fact(7)
  print(res)

#iterative o(n) o(1)
class Solution:
  def factorial(self,n:int)->int:
    fact=1
    for i in range(1,n+1):
        fact=i*fact
    return fact
   

if __name__=="__main__":
  sol=Solution()
  res=sol.factorial(4)
  print(res)
