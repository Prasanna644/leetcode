class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Simple sorted approach
        return sorted(s) == sorted(t)
