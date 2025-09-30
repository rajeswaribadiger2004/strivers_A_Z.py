import math
class Solution:
  def isPrime(self,n:int)->bool:
    if n<=1:
      return false
    if n==2:
      return true

    count=0
    for i in range(1,int(math.sqrt(n))+1):
      if n%i==0:
        count+=1

      if n//i==i:
        count+=1

    return count==2

if __name__=="__main__":
    sol=Solution()
n=123
print(sol.isPrime(n))
