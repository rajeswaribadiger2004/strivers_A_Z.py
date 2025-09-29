class solution:
  def palindrome(self,n:int)->bool:
    revNo=0
    dup=n
    while n>0
      dig=n%10
      revNo=(revNo*10)+dig
      n=n//10
    return dup==revNo
