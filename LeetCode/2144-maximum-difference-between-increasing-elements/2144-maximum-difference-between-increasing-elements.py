class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        maxdiff = -1

        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                maxdiff = max(maxdiff, nums[j] - nums[i])
            elif nums[j] < nums[i]:
                i = j  

        return maxdiff

        