#FindFirstandLastPositionOfElementInSortedArray
#practically faster than use binary search for both upper and lower bound
#cause there are not so many continues target value in the dataset
class Solution(object):    
    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = int((left+right)/2)
            if nums[mid]>= target:
                right = mid
            else:
                left = mid+1
        return left
    
    def searchRange(self, nums, target):
        if nums == []: return [-1, -1]
        #find the lower bound of the element
        lower_pos = self.lower_bound(nums, target)
        #check the validity of return value
        if(lower_pos == len(nums) or nums[lower_pos]!=target):
            return [-1, -1]

        #find the upper bound 
        upper_pos = lower_pos
        while upper_pos<len(nums):
            if nums[upper_pos]!=target:
                break
            upper_pos+=1       
        return [lower_pos, upper_pos]