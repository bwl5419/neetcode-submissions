class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) +1 
        pairs = []
        for num, freq in count.items():
            pairs.append([freq,num])
        pairs.sort(reverse= True)
        result = []
        for i in range(k):
            result.append(pairs[i][1])

        return result 
            

        

