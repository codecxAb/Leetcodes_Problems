class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1= s.strip()
        s1 = s1.split(" ")
        
        l = s1[-1]
        n = len(l)
        return n
        
        