class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # count the frequency of the each letter from respective string.
            countT[t[i]] = 1 + countT.get(t[i], 0) # ''

        for el in s:
            if countS[el] != countT.get(el, 0):
                return False
        
        return True
        