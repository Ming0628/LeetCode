class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 1 or k < 0:
            return False
        else:
            dic = {}
            for i in range(len(nums)):
                if nums[i] in dic:
                    if i - dic[nums[i]] <= k:
                        return True
                    else:
                        dic[nums[i]] = i
                else:
                    dic[nums[i]] = i
            return False

test = Solution()
print test.containsNearbyDuplicate([2, 1, 0, 2, 3, 4], 2)
print test.containsNearbyDuplicate([2], 0)
print test.containsNearbyDuplicate([1, 0, 1, 1], 1)
