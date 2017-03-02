class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for e in nums:
            if (target - e) in nums:
                temp = nums[nums.index(e) + 1:]
                if (target - e) in temp:
                    res.append(nums.index(e))
                    res.append(temp.index(target - e) + nums.index(e) + 1)
                    return res
        return

    
test = Solution()
print test.twoSum([2, 7, 11, 15], 9)
print test.twoSum([2, 7, 11, 15], 17)
print test.twoSum([2, 7, 11, 11, 11, 11], 22)
print test.twoSum([3, 2, 4], 6)
print test.twoSum([3, 3], 6)
