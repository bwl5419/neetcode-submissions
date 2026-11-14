class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            content = [0] *26
            for c in word:
                content[ord(c)- ord("a")] +=1
            key= tuple(content)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())

