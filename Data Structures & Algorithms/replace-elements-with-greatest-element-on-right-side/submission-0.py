class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prevMax = -1
        for i in range(n - 1, -1, -1):
            prevMax, arr[i] = max(prevMax, arr[i]), prevMax

        arr[-1] = -1
        return arr