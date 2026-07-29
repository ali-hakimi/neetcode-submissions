class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        # B 1 2 3 4 5 
        # A 1 2 3

        total = len(A) + len(B) # 8
        half = total // 2 # 4

        if len(B) < len(A):
            B, A = A, B

        l, r = 0, len(A) - 1 # l = 0, r = 2
        while True:
            i = (l + r) // 2 # i = 1
            j = half - i - 2 # 4 - 1 - 2 = 1

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Aright:
                # partition is correct
                # odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    #even
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1


