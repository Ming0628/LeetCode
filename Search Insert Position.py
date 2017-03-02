class Solution(object):
        def searchInsert(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            if target in nums:
                return nums.index(target)
            else:
                if target < nums[0]:
                    return 0
                elif target > nums[len(nums) - 1]:
                    return len(nums)
                else:
                    for e in nums:
                        if e < target and nums[nums.index(e) + 1] > target:
                            return nums.index(e) + 1

        def searchInsert2(self, nums, target):
                return len([x for x in nums if x < target])

test = Solution()
my_list = [1, 3, 5, 6]
print test.searchInsert2(my_list, 5)
print test.searchInsert2(my_list, 2)
print test.searchInsert2(my_list, 7)
print test.searchInsert2(my_list, 0)
