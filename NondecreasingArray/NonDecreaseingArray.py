#wrong case [-1,4,2,3]
#wrong case [3,4,2,3]]
#test case [4,2,3]
#test case [4,2,1]
class Solution(object):
    def checkPossibility(self, nums):

        numOfDecreasing = 0
        DecreasingOccurPlace = 0
        SmallerThanPrevTwo = 0


        for i in range(1, len(nums)):
            if(i==DecreasingOccurPlace+2 and i-2>0):
                if(nums[i]<nums[i-2] and nums[i-1]<nums[i-3]):
                    SmallerThanPrevTwo = SmallerThanPrevTwo+1
            if(nums[i]<nums[i-1]):
                numOfDecreasing+=1
                DecreasingOccurPlace = i-1



        if numOfDecreasing >= 2 or SmallerThanPrevTwo>0:
            return False
        return True
        