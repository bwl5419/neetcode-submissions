class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        content = {}
        for letter in s:
            if letter not in content:
                content[letter] =1
            else:
                content[letter] +=1
        content2 ={}
        for letter in t:
            if letter not in content2:
                content2[letter] =1
            else:
                content2[letter] +=1
        if content != content2:
            return False
        return True
        
        