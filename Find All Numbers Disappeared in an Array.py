class Solution(object):
    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n < 1:
            return []
        else:
            temp = [val for val in range(1, n + 1)]
            nums[:] = list(set(nums))
            return [i for i in temp if i not in nums]

    def findDisappearedNumbers2(self, nums):
        n = len(nums)
        if n < 1:
            return []
        else:
            res = []
            for i in range(n):
                if nums[i] != i + 1 and i + 1 not in nums:
                    res.append(i + 1)
            return res

    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))

test = Solution()
print test.findDisappearedNumbers([1, 1])
print test.findDisappearedNumbers([1, 1, 2])
print test.findDisappearedNumbers([])
print test.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
