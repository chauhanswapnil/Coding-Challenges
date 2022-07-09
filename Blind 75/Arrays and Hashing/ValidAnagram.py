class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHashMap = {}
        for c in s:
            if c in sHashMap:
                sHashMap[c] += 1
            else:
                sHashMap[c] = 1

        tHashMap = {}
        for c in t:
            if c in tHashMap:
                tHashMap[c] += 1
            else:
                tHashMap[c] = 1
        
        return sHashMap == tHashMap