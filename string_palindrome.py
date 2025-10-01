class Solution:
    def pal(self,s:str)->bool:
        left,right=0,len(s)-1
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        if s[left].lower()!=s[right].lower():
            return False
        else:
            left += 1
            right -= 1
        return True
if __name__=="__main__":
    sol=Solution()
    print(sol.pal("ABCDCBA")) 
