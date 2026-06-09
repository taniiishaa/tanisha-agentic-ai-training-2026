class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        hash_map={}

        for i in range(0,n):
            rem = target - nums[i]
            if rem in hash_map :
                return [hash_map[rem],i]
            else :
                hash_map[nums[i]] = i 
nums = [2,7,11,15]
target = 9
obj = Solution()
result = obj.twoSum(nums , target)
print(result)  