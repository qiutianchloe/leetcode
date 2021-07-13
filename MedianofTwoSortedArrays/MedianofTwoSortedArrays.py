class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # make sure A is shorter array
        A,B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2
        
        if len(A)>len(B):
            A, B = B, A

        #return the value when there is only one value in two lists
        if len(A)==0 and len(B)==1:
            return B[0]
        
        left, right = 0, len(A)-1
        while True:
            # index point to the left most of the left partition
            i = (left+right)//2 # index for A
            j = half-i-2              # index for B
            
            #get the value of each partition edge

            if i>=0: Aleft = A[i]
            else:  Aleft = float("-infinity")
                
            if (i+1)<len(A): Aright = A[i+1]
            else: Aright = float("infinity")
                
            if j>=0: Bleft = B[j]
            else:  Bleft = float("-infinity")
                
            if (j+1)<len(B): Bright = B[j+1]
            else: Bright = float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                if total%2: return min(Aright, Bright)
                else: return (max(Aleft, Bleft)+min(Aright, Bright))/2
            elif Aleft>Bright:
                right = i-1
            else:
                left = i+1
