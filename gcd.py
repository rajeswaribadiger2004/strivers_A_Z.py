class Solution:
  def gcd(self,a:int,b:int)->int:
    while a>0 and b>0:
      if a>b:
        a=a%b
      else:
        b=b%a
    return b if a==0 else a

#     s = Solution()
# print(s.gcd(20, 15))  # Output: 5
# print(s.gcd(100, 80)) # Output: 20
# print(s.gcd(7, 3))    # Output: 1
