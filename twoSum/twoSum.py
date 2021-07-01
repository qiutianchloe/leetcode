def twoSum( nums, target):
    num_pos_dic = {}
    for i in range(len(nums)):
        if target - nums[i] in num_pos_dic:
            return [num_pos_dic[target - nums[i]],i]
        else:
            num_pos_dic[nums[i]]=i

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))