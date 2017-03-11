class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        originalLen = len(nums)
        temp = nums + nums
        nums[:] = temp[len(temp) - k - originalLen: len(temp) - k]


a = [1, 2]
test = Solution()
test.rotate(a, 1)
print a
