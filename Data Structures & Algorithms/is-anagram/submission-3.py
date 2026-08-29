class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [ord(char) for char in s]
        l2 = [ord(char) for char in t]
        return True if (sorted(l1)) == (sorted(l2)) else False
        