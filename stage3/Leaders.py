class Solution:
    def printLeaders(self, arr: List[int], n: int) -> List[int]:
        ans = []
        max_elem = arr[n - 1]
        ans.append(arr[n - 1])

        # Traverse from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] > max_elem:
                ans.append(arr[i])
                max_elem = arr[i]

        # Reverse to maintain original order of leaders
        ans.reverse()
        return ans

  #o(n)
