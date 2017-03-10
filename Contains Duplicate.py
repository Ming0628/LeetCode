class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


test = Solution()
print test.containsDuplicate([1])
print test.containsDuplicate([1, 2])
print test.containsDuplicate([1, 1])
print test.containsDuplicate([0, 1, 2, 1])
