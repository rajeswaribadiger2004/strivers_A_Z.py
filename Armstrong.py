#sum of the digit raise to the power of length of no equal to total
class Solution:
  def armstrong(self,num:int)->bool:
    k=len(str(num))
    n=num
    total=0
    while n>0:
      dig=n%10
      total += dig ** k     
      n//=10
    return total==num
    
s = Solution()
print(s.armstrong(153))
#o(n)
#o(n)