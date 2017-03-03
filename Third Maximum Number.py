class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNumber = max(nums)
        temp = [x for x in nums if x != maxNumber]
        if len(temp) < 1:
            return maxNumber
        else:
            secondMax = max(temp)
            temp2 = [x for x in temp if x != secondMax]
            if len(temp2) < 1:
                return maxNumber
            else:
                return max(temp2)

            
test = Solution()
print test.thirdMax([3, 2, 1])
print test.thirdMax([1, 2])
print test.thirdMax([2, 2, 3, 1])
    
