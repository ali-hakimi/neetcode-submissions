class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            newPerms = []
            for p in perms:
                for j in range(len(p) + 1):
                    copy = p.copy()
                    copy.insert(j, n)
                    newPerms.append(copy)
            perms = newPerms
        return perms