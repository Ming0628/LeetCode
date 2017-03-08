class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strNum = ''.join(str(num) for num in digits)
        return map(int, str(int(strNum) + 1))
        

test = Solution()
print test.plusOne([1, 2, 3, 9])
