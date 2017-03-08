class Solution(object):
    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = max(nums)
        for i in range(len(nums) - 1, 0, -1):
            for j in range(len(nums)):
                if j + i <= len(nums):
                    if sum(nums[j:j + i]) > maxSum:
                        maxSum = sum(nums[j: j + i])
        return maxSum

    def maxSubArray(self, nums):
        if len(nums) < 1:
            return
        else:
            temMax = res = nums[0]
            """
            initial the variable to be the first element in the list
            instead of 0 to prevent the first element is negative
            """
            for e in nums[1:]:
                temMax = max(e, temMax + e)
                res = max(temMax, res)
            return res
