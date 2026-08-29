class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Checking if same length
        if len(s) != len(t):
            return False

        #Creating array with 26 empty indices
        s_count = [0] * 26 
        t_count = [0] * 26 
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            t_count[ord(t[i]) - ord('a')] += 1
        
        #Final checking if anagram
        return True if s_count == t_count else False