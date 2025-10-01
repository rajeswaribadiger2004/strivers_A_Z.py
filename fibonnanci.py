# Recursion with Memoization, also known as Top-Down Dynamic Programming (DP).      o(2^n) o(n)
class Solution:
  def __init__(self):
    self.memo={}
  def fib(self,n:int)->int:
    if n<=1:
      return n
    if n in self.memo:
      return self.memo[n]
    self.memo[n]=self.fib(n-1)+self.fib(n-1)
    return self.memo[n]
if __name__=="__main__":
    sol=Solution()
    n=4
    for i in range(n+1):
        print(sol.fib(i), end=" ")
      
