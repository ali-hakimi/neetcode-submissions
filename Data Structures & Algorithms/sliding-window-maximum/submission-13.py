class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()
        l = r= 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l +=1
            if l > q[0]:
                q.popleft()

            
            r+=1

        return output