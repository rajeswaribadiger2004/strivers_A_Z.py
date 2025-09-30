class Solution:
    def printNumbers(self, cnt: int = 0) -> None:
        # Base case
        if cnt == 3:
            return
        
        # Print current number
        print(cnt)
        
        # Recursive call
        self.printNumbers(cnt + 1)


# Example usage (like test case in LeetCode)
if __name__ == "__main__":
    sol = Solution()
    sol.printNumbers()
