class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = cursum = nums[0]
        for i in range(1, len(nums)):
            cursum += nums[i]
            if (nums[i] == 0 and nums[i - 1] == 1) or (i == len(nums) - 1):
                maxsum = max(maxsum, cursum)
                cursum = 0
        return maxsum


test = Solution()
print test.findMaxConsecutiveOnes([1, 0, 0, 0, 0])
print test.findMaxConsecutiveOnes([1, 0, 0, 0, 1, 1])
print test.findMaxConsecutiveOnes([1, 1, 0, 0, 0, 1, 1, 1, 0, 0])
