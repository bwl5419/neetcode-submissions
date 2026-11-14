class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        content = {}
        for i in range(len(s)):
            content[s[i]] = content.get(s[i],0)+1
            content[t[i]] = content.get(t[i],0) -1 

        for val in content.values():
            if val != 0:
                return False
        return True



          
        