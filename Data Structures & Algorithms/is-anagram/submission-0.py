class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for letters in s:
            if letters in d1:
                d1[letters] += 1
            else:
                d1[letters] = 1

        for letters in t:
            if letters in d2:
                d2[letters] += 1
            else:
                d2[letters] = 1
        if d1 == d2:
            return True
        else:
            return False
        
        
        