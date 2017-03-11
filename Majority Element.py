import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countList = collections.Counter(nums)
        for key in countList:
            if countList[key] > len(nums) / 2:
                return key


test = Solution()
print test.majorityElement([1, 1, 1, 2, 2, 2, 2, 2, 3])
