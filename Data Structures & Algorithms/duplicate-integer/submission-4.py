# Hashmap solution
# Space: O(n) -> set of nums
# Time: O(n) -> over nums

# [1, 2, 3, 4]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)