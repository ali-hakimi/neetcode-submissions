class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum, res = 0, 0
        prefixSums = { 0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        return res