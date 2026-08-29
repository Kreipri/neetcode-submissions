class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if (sorted(list(ord(char) for char in s))) == (sorted(list(ord(char) for char in t))) else False