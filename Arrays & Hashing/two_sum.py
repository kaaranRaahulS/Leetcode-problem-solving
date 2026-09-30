class Solution:
    #This solution works only when the array is sorted
    #Time complexity is O(n log n)
    #Space complexity is O(1)
    def twoSum_sorted_array(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []
        i = 0 
        j = len(nums) - 1 
        while(1):
            if(nums[i] + nums[j] == target and i != j):
                return [i, j]
            elif (nums[i] + nums[j] < target):
                i += 1
            elif (i == j):
                return []
            else: 
                j -= 1

    #Time complexity is O(n) and space complexity is O(n)
    def twoSum_unsorted_array(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
        return []

two_sum = Solution().twoSum_unsorted_array([3,4,5,6], 7)
print(two_sum)