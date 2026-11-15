class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        content = {}
        for ch in s1:
            content[ch] = content.get(ch,0) + 1
        for r in range(len(s1), len(s2)+1):
            guess = s2[l:r]
            cont= {}
            for ch in guess:
                cont[ch] = cont.get(ch,0) +1
            if cont == content:
                return True
            l+=1
        return False

