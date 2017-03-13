import collections


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return
        else:
            counter = collections.Counter(nums)
            for val in counter:
                if counter[val] > 1:
                    return val
