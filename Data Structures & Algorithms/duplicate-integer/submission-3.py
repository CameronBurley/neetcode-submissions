# Hashmap solution
# Space: O(n) -> set of nums
# Time: O(n) -> over nums

# [1, 2, 3, 4]

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False