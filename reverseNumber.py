class solution:
  def reverseNum(self,n:int)->int
    revNo=0
    while n>0:
      digit=n%10
      revNo=(revNo*10)+digit
      n=n//10
    return revNo

# s = Solution()
# print(s.reverseNumber(12345))   # Output: 54321
# print(s.reverseNumber(120))     # Output: 21
# print(s.reverseNumber(7))       # Output: 7
