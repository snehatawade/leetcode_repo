class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i]+nums[j]==target:
                    self = [i,j]
                    return self
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        