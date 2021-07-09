class Solution(object):
    def singleNonDuplicate(self, nums):
        def is_single(pos):
            return nums[pos]!=nums[pos-1] and nums[pos]!=nums[pos+1]
        def check_duplicate(pos):
            #the position is an odd value
            if pos%2==1:
                if nums[pos]==nums[pos-1]:return True
                else: return False
            #the position is an even value
            else:
                if nums[pos]==nums[pos+1]: return True
                else: return False
        
        #in the case there is only one element for the input 
        if len(nums)==1: return nums[0]

        #check the first and last element
        left, right = 0, len(nums)-1
        if nums[left]!=nums[left+1]:return nums[left]
        elif nums[right]!=nums[right-1]:return nums[right]

        while left<=right:
            mid = (int)((left+right)/2)
            if is_single(mid):
                return nums[mid]

            #the left part do not have the single value
            if check_duplicate(mid):
                left = mid + 1
            else:
                right = right - 1
                

        return -1
                

ob = Solution()
# lis = [1,1,2,3,3,4,4,8,8]
lis = [3,3,7,7,10,11,11]
# lis = [5]
# lis = [0, 0, 1, 1, 2, 2, 3, 3, 5]
# lis = [0, 1, 1, 2, 2, 3, 3, 5, 5]
result = ob.singleNonDuplicate(lis)
print(result)
                