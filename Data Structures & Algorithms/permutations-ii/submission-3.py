class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = [[]]
        for i in range(len(nums)):
            newPerms = []
            for p in perms:
                for j in range(len(p) + 1):
                    if j > 0 and nums[i] == p[j - 1]:
                        break
                    copy = p.copy()
                    copy.insert(j, nums[i])
                    newPerms.append(copy)
            perms = newPerms
        return perms
