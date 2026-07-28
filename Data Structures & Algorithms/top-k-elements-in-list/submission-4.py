class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        for num, count in countMap.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        