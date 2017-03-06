class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.append(nums.pop(i))

                
nums = [0, 1, 2, 0, 3, 3, 0, 0, 0, 0, 0, 9, 8, 0, 8, 0, 2]
test = Solution()
test.moveZeroes(nums)
print nums
