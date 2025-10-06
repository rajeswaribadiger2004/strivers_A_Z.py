ass Solution:
    def maxProfit(self, arr: List[int]) -> int:
        minPrice=float('inf')
        maxPro=0
        for i in range(len(arr)):
            minPrice=min(minPrice,arr[i])
            maxPro=max(maxPro,arr[i]-minPrice)
        return maxPro

#0(1) o(n)
