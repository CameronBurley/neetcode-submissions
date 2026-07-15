# Time Complexity = O(n)
# Space = O(n + m)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(t) != len(s)):
            return False
        
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return True