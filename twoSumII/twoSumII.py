class Solution(object):
    def twoSum(self, nums, target):
        left, right = 0, len(nums)-1
        
        while right>left:
            sums = nums[left]+nums[right]
            if sums==target:
                break
            elif sums<target:
                left = left+1
            else:
                right = right-1
                
        return [left+1, right+1]

ob = Solution()
result = ob.twoSum([2,7,11,15], 9)
print(result)