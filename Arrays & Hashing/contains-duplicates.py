class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

hasDuplicates = Solution().hasDuplicate
print(hasDuplicates([1, 2, 3, 4, 5, 5]))