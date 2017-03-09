class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[0] != 0:
            return 0
        else:
            first = nums[0]
            last = nums[len(nums) - 1]
            if first + len(nums) - 1 == last:
                return last + 1
            else:
                expectSum = (first + last) * (len(nums) + 1) / 2
                return expectSum - sum(nums)


test = Solution()
print test.missingNumber([1, 2, 3])
print test.missingNumber([0, 1, 3])
print test.missingNumber([0, 1, 2, 4])
print test.missingNumber([0, 1])
print test.missingNumber([1, 0])
