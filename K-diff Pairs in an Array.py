import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > 0:
            return len(set(n for n in nums) & set(n + k for n in nums))
        elif k == 0:
            return sum(n > 1 for n in collections.Counter(nums).values())
        else:
            return 0


test = Solution()
print test.findPairs([1, 2, 3, 4, 5, 6, 7], 2)
print test.findPairs([3, 1, 4, 1, 5], 2)
print test.findPairs([1, 1, 1, 1, 2, 2, 2], 0)
