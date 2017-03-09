class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (0 + len(nums)) * (len(nums) + 1) / 2 - sum(nums)

            
test = Solution()
print test.missingNumber([1, 2, 3])
print test.missingNumber([0, 1, 3])
print test.missingNumber([0, 1, 2, 4])
print test.missingNumber([0, 1])
print test.missingNumber([1, 0])
