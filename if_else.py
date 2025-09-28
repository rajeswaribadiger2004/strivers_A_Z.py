class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks >= 70:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        elif marks >= 35:
            print("Grade D")
        else:
            print("Fail")

# Example usage:
s = Solution()
s.studentGrade(95)   # Output: Grade A
s.studentGrade(68)   # Output: Grade C
s.studentGrade(20)   # Output: Fail
