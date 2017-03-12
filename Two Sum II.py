class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # res = []
        # sub = [target - n for n in numbers]
        # temp = [val for val in numbers if val in sub]
        # if len(temp) == 2:
        #     first = numbers.index(temp[0])
        #     second = numbers[first + 1:].index(temp[1]) + first + 1
        #     res[:] = [first + 1, second + 1]
        # else:
        #     for i in temp:
        #         if i != (target / 2):
        #             res.append(numbers.index(i) + 1)
        # return res
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s > target:
                r -= 1
            else:
                l += 1


test = Solution()
print test.twoSum([1, 2, 3, 4], 6)
print test.twoSum([1, 2, 4, 5], 5)
print test.twoSum([-1, 0, 1], 0)
print test.twoSum([0, 1, 2, 3, 4, 0], 0)
