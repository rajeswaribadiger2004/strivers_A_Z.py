class Solution:
  def paranthesis(self,s:str):
    result=""
    level=0
    for char in s:
      if char==")":
        if level>0:
          result+=char
        level+=1
      else:
        level-=1
      if level>=0:
        result+=char
        return result

#o(n)
