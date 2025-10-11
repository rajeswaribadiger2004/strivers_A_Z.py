from typing import List
class Solution:
    def merge(self,left:list[int],right:list[int])->list[int]:
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
                    # Append remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    def mergeSort(self,arr:list[int])->list[int]:
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
if __name__ == "__main__":
    sol = Solution()
    arr = [4, 2, 6, 5, 7, 3, 1]
    print("Before Sorting:", arr)
    sorted_arr = sol.sortArray(arr)
    print("After Merge Sort:", sorted_arr)


#Time complexity: O(nlogn) 
#Space complexity: O(n)  
      
