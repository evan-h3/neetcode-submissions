class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        length = len(nums1) + len(nums2)
        half = length // 2

        if len(A) > len(B):
            A, B = B, A
        
        l , r = 0 , len(A)-1

        while True:
            i = (l+r) // 2 #A
            j = half - i - 1 - 1 #B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if length % 2 != 0:
                    return min(Aright, Bright)
                #even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        
