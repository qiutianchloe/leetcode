class Solution(object):
    def merge(self, nums1, m, nums2, n):
        pointer = m + n -1
        while(m> 0 and n>0):
            if(nums1[m-1] > nums2[n-1]):
                nums1[pointer] = nums1[m-1]
                m=m-1
                pointer = pointer-1
                
            else:
                nums1[pointer]=nums2[n-1]
                n=n-1
                pointer = pointer-1
                
                
        while(n>0):
            nums1[pointer] = nums2[n-1]
            n=n-1
            pointer = pointer-1
        print(nums1)


ob = Solution()
ob.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)