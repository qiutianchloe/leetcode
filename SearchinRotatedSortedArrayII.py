#Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums, target):
        #define left and right value
        left, right = 0, len(nums)-1

        
        #while loop, gate is left < right, the same as other binary search
        while left <= right:
            #calculate the mid 
            mid = int((left+right)/2)
            #return value when num[mid] is our target
            if nums[mid] == target:
                return True
            
            #make sure that when nums[left]==nums[mid]
            #the left are sorted 
            while left<mid and nums[left]==nums[mid]:
                left += 1
            
            #left part of nums are sorted
            if(nums[left]<=nums[mid]):
                if nums[mid]<target or nums[left]>target:
                    left = mid+1
                else:
                    right = mid-1
                
            #right part of nums are sorted 
            else:
                if nums[mid]>target or nums[right]<target:
                    right = mid-1
                else:
                    left = mid+1
        
        # when the loof stop but still didn't find the result
        # the target don't exist, return -1
        
        return False
