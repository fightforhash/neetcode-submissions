class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False
 
        freq = {}
        
        for c in s:
            freq[c] = freq.get(c,0) + 1

        for j in t:
            freq[j] = freq.get(j,0) - 1 

        for k in s:
            if (freq[k] != 0):
                return False
            
      
        return True
        