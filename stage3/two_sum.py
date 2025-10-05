class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(arr):
            if target-num in seen:
                return [seen[target-num],i]
            seen[num]=i
        return[-1,-1]
