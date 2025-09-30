mport math

class Solution:
    def findDivisors(self, n: int) -> list[int]:
        divisors = []
        sqrtN = int(math.sqrt(n))

        for i in range(1, sqrtN + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)

        return sorted(divisors)


# Example usage (like test cases in LeetCode)
if __name__ == "__main__":
    sol = Solution()
    number = 12
    print("Divisors of", number, "are:", sol.findDivisors(number))

