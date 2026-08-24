class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        m = len(nums) // 2
        return self.merge(self.sortArray(nums[:m]), self.sortArray(nums[m:]))

    def merge(self, nums1, nums2):
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        res.extend(nums1[i:])
        res.extend(nums2[j:])
        return res
