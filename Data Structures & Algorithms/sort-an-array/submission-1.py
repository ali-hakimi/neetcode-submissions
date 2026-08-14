class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        l, r = 0, 0

        res = []
        while l < len(left) and r < len(right):
            print(l, r)
            if left[l] < right[r]:
                res.append(left[l])
                l+=1
            else:
                res.append(right[r])
                r+=1
        res = res + left[l:] + right[r:]
        return res