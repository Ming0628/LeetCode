class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return res
        else:
            res = [1]
            for counter in range(rowIndex):
                res = map(lambda x, y: x + y, [0] + res, res + [0])
            return res


test = Solution()
print test.getRow(4)
print test.getRow(0)
print test.getRow(1)
print test.getRow(2)
