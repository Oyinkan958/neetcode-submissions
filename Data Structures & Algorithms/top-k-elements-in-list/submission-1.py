class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            if num in numFreq:
                numFreq[num] = numFreq[num] + 1
            else:
                numFreq[num] = 1
        numbers = list(numFreq.keys())
        numbers.sort(key=lambda num: numFreq[num], reverse=True)
        return numbers[:k]
        