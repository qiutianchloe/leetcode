class Solution(object):
    def upper_bound(self, nums, target):
        left, right = 0, len(nums)
        while left<right:
            mid = int((left+right)/2)
            if nums[mid]>target:
                right = mid
            else:
                left = mid + 1
        return left
    
    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = int((left+right)/2)
            if nums[mid] >= target:
                #in the case we find the target value, we still try to find another on in left part of the list 
                right = mid
            else:
                left = mid+1
        return left
    
    def searchRange(self, nums, target):
        if nums == []: return [-1, -1]
        #find the upper bound of the target value
        upper_pos = self.upper_bound(nums, target)-1 #return value of upper bound need minus 1
        #find the lower bound of the target value 
        lower_pos = self.lower_bound(nums, target)
        #check the validity of return value
        if(lower_pos == len(nums) or nums[lower_pos]!=target):
            return [-1, -1]

        return [lower_pos, upper_pos]