class Solution(object):
    def removeDuplicates(self, nums):
        # remove some special case:
        if len(nums)==0:return 0
        if len(nums)==1:return 1
        
        # two pointers: 
        # slow pointer point to the current distinct value 
        # fast pointer used to find the distinct value
        slow, fast = 0, 1
        while fast<len(nums):
            slowvalue = nums[slow]
            if nums[fast]!=slowvalue:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast+1
        return slow+1

ob = Solution()
lis = [0,0,1,1,1,2,2,3,3,4]
# lis = [1,1,2]
result = ob.removeDuplicates(lis)
print(result)
        