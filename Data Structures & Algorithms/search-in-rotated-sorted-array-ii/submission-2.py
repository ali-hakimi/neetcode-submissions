class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            # Left half is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # Right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


        # 1 2 3 4 5 
        # 2 3 4 5 1 
        # 3 4 5 1 2 
        # 4 5 1 2 3 @
        # 5 1 2 3 4 @